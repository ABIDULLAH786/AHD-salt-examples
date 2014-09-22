

class MyClass(GeneratedClass):

    def onLoad(self):
        self.isRunning = False
        self.startConnectId = None
        self.finishConnectId = None
        self.tabletService = None
        self.frameManager = None
        try:
            self.frameManager = ALProxy("ALFrameManager")
        except Exception as e:
            self.logger.error(e)

    def onUnload(self):
        if self.tabletService:
            self.tabletService.stopVideo()
            self.disconnectStartedListener()
            self.disconnectFinishedListener()
            self.isRunning = False

    def disconnectFinishedListener(self):
        if self.finishConnectId and self.tabletService:
            try:
                self.tabletService.videoFinished.disconnect(self.finishConnectId)
                self.finishConnectId = None
            except Exception as e:
                self.logger.error(e)

    def disconnectStartedListener(self):
        if self.startConnectId and self.tabletService:
            try:
                self.tabletService.videoStarted.disconnect(self.startConnectId)
                self.startConnectId = None
            except Exception as e:
                self.logger.error(e)

    def _getTabletService(self):
        tabletService = None
        try:
            tabletService = self.session().service("ALTabletService")
        except Exception as e:
            self.logger.error(e)
        return tabletService

    def _getAppName(self):
        import os
        if self.frameManager:
            behaviorPath = os.path.normpath(self.frameManager.getBehaviorPath(self.behaviorId))
            appsFolderFragment = os.path.join("PackageManager", "apps")
            if not (appsFolderFragment in behaviorPath):
                self.logger.error("appsFolderFragment is not in behaviorPath")
            fragment = behaviorPath.split(appsFolderFragment, 1)[1]
            return fragment.lstrip("\\/")
        else:
            self.logger.warning("No ALFrameManager")

    def _getAbsoluteUrl(self, partialUrl):
        import os
        subpath = os.path.join(self._getAppName(), os.path.normpath(partialUrl).lstrip("\\/"))
        if self.tabletService:
            return "http://%s/apps/%s" % (self.tabletService.robotIp(), subpath.replace(os.path.sep, "/"))
        else:
            self.logger.warning("No ALTabletService, can't get robot Ip.")
            return None

    def connectStartCallback(self):
        try:
            self.startConnectId = self.tabletService.videoStarted.connect(self.onVideoStarted)
        except Exception as err:
            self.logger.warning("Failed to subscribe to started callback: %s " % err)

    def connectStopCallback(self):
        try:
            self.finishConnectId = self.tabletService.videoFinished.connect(self.onVideoFinished)
        except Exception as err:
            self.logger.warning("Failed to subscribe to stopped callback: %s " % err)

    def onInput_onStart(self):
        if self.isRunning:
            return # already running, nothing to do
        self.isRunning = True
        # We create TabletService here in order to avoid
        # problems with connections and disconnections of the tablet during the life of the application
        self.tabletService = self._getTabletService()
        if self.tabletService:
            try:
                url = self.getParameter("VideoPath")
                if url == '':
                    self.logger.error("URL of the video is empty")
                if not url.startswith('http'):
                    url = self._getAbsoluteUrl(url)
                self.connectStartCallback()
                self.connectStopCallback()
                self.tabletService.playVideo(url)
            except Exception as err:
                self.logger.warning("Error during playVideo or subscribe: %s " % err)
                self.onStopped()
                self.isRunning = False
        else:
            self.logger.warning("No ALTabletService, can't play video.")
            self.onStopped()
            self.isRunning = False

    def onInput_onStop(self):
        self.onUnload()
        self.onStopped()

    def onInput_onPauseVideo(self):
        if self.tabletService:
            self.tabletService.pauseVideo()

    def onInput_onResumeVideo(self):
        if self.tabletService:
            self.tabletService.resumeVideo()

    def onVideoStarted(self):
        self.disconnectStartedListener()
        self.onStarted()

    def onVideoFinished(self):
        self.disconnectFinishedListener()
        self.onStopped()
        self.isRunning = False
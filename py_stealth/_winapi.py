
from ctypes.wintypes import *
import ctypes  # py2


__author__ = 'ZeroDX'
__version__ = 1.1


FM_GETFOCUS = 0x600
PM_REMOVE = 0x1
WM_COPYDATA = 0x4A

LRESULT = LPARAM
PVOID = ctypes.c_char_p
ULONG_PTR = LPARAM

if 'LPMSG' not in dir():  # py2
    LPMSG = ctypes.POINTER(MSG)


class COPYDATA(ctypes.Structure):
    _fields_ = [('dwData', ULONG_PTR),
                ('cbData', DWORD),
                ('lpData', PVOID)]

    @property
    def pointer(self):
        return ctypes.byref(self)


GetCurrentProcessId = ctypes.windll.kernel32.GetCurrentProcessId
GetCurrentProcessId.restype = DWORD

GetCurrentThreadId = ctypes.windll.kernel32.GetCurrentThreadId
GetCurrentThreadId.restype = DWORD

GetLastError = ctypes.windll.kernel32.GetLastError
GetLastError.restype = DWORD

FindWindow = ctypes.windll.user32.FindWindowW
FindWindow.restype = HWND
FindWindow.argtypes = (LPCWSTR,  # _In_opt_ lpClassName
                       LPCWSTR)  # _In_opt_ lpWindowName

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox.restype = INT
MessageBox.argtypes = (HWND,     # _In_opt_ hWnd
                       LPCWSTR,  # _In_opt_ lpText
                       LPCWSTR,  # _In_opt_ lpCaption
                       UINT)     # _In_ uType

PeekMessage = ctypes.windll.user32.PeekMessageW
PeekMessage.restype = BOOL
PeekMessage.argtypes = (LPMSG,  # _Out_ lpMsg
                        HWND,   # _In_opt_ hWnd
                        UINT,   # _In_ wMsgFilterMin
                        UINT,   # _In_ wMsgFilterMax
                        UINT)   # _In_ wRemoveMsg

SendMessage = ctypes.windll.user32.SendMessageW
SendMessage.restype = LRESULT
SendMessage.argtypes = (HWND,             # _In_ hWnd
                        UINT,             # _In_ Msg
                        WPARAM,           # _In_ wParam
                        ctypes.c_void_p)  # _In_ lParam

SetLastError = ctypes.windll.kernel32.SetLastError
SetLastError.argtypes = (DWORD,)  # _In_ dwErrCode

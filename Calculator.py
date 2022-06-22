import ctypes
from MyStruct import MyKinematicParam, MCS, BCS

class Calculator:
    def __init__( self ):
        self.mydll = None
        self._Dll_InitKinematic = None
        self._Dll_DeinitKinematic = None
        self._Dll_GetVersionInfo = None
        self._Dll_ConfigParameter = None
        self._Dll_ForwardKinematic = None
        self._Dll_InverseKinematic = None

        self.Test = None

    def LoadDll( self ):
        self.mydll = ctypes.WinDLL( './KinematicTx.dll' )

        # @1
        self._Dll_InitKinematic = self.mydll[ 1 ] # init kinematic
        self._Dll_InitKinematic.restype = ctypes.c_bool

        # @2
        self._Dll_DeinitKinematic = self.mydll[ 2 ] # deinit kinematic

        # @3
        self._Dll_GetVersionInfo = self.mydll[ 3 ] # version info

        # @4
        self._Dll_ConfigParameter = self.mydll[ 4 ] # config parameter
        self._Dll_ConfigParameter.argtypes = [ MyKinematicParam ]
        self._Dll_ConfigParameter.restype = ctypes.c_int32

        # @5
        self._Dll_ForwardKinematic = self.mydll[5]
        self._Dll_ForwardKinematic.argtypes = [ctypes.POINTER(MCS), ctypes.POINTER(BCS)]
        self._Dll_ForwardKinematic.restype = ctypes.c_bool

        # @6
        self._Dll_InverseKinematic = self.mydll[6]
        self._Dll_InverseKinematic.argtypes = [ctypes.POINTER(BCS), ctypes.POINTER(MCS), ctypes.POINTER(MCS)]
        self._Dll_InverseKinematic.restype = ctypes.c_bool

        # @7
        self._Test = self.mydll[ 7 ] # test, return true

    def InitKinematic( self, nKinematicType ):
        if( self._Dll_InitKinematic == None ):
            print( 'Error' )

        self._Dll_InitKinematic( nKinematicType )

    def DeInitKinematic( self ):
        if (self._Dll_DeInitKinematic == None):
            print('Error')

        self._Dll_DeInitKinematic()

    def GetVersionInfo( self ):
        if (self._Dll_GetVersionInfo == None):
            print('Error')

        return hex( self._Dll_GetVersionInfo() )

    def ConfigParameter( self ):
        if (self._Dll_ConfigParameter == None):
            print('Error')
        TempParam = MyKinematicParam(nKinematicType=3,
                                     nToolAxisDirection=3,
                                     nRA=0,
                                     nRB=0,
                                     nAxisDirection_First=2,
                                     nAxisDirection_Second=3,
                                     nRotationDirection_First=1,
                                     nRotationDirection_Second=2,
                                     nRestrict_First=(0, 0),
                                     nRestrict_Second=(0, 0),
                                     nToolHolderLength=229000,
                                     nRotationOffset_First=(0, 0, 0),
                                     nRotationOffset_Second=(0, 0, 0),
                                     nPr3021to3023=(10, 0, 0),
                                     nPr3024to3026=(0, 0, 0),
                                     nPr3031to3033=(0, 0, 0),
                                     nPr3034to3036=(0, 0, 0),
                                     nPr3041to3043=(0, 0, 0),
                                     nPr3044to3046=(-1645900, -79500, 0),
                                     nIntMode=0,
                                     nTableCrdMode=1,
                                     nToolLength=0,
                                     G54Offset=(0, 0, 0, 0, 0)
                                     )
        bResult = self._Dll_ConfigParameter(TempParam)
        print(bResult)

    def ForwardKinematic( self ):
        if (self._Dll_ForwardKinematic == None):
            print('Error')

        c = MCS(coord=(ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(15000),
                       ctypes.c_double(30000)))

        d = BCS(coord=(ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0)))
        e = self._Dll_ForwardKinematic(ctypes.pointer(c), ctypes.pointer(d))
        print(c.coord[0], c.coord[1], c.coord[2], c.coord[3], c.coord[4])
        print(d.coord[0], d.coord[1], d.coord[2], d.coord[3], d.coord[4])
        print(e)
        return d

    def InverseKinematic( self ):
        if (self._Dll_InverseKinematic == None):
            print('Error')

        h = BCS(coord=(ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(15000),
                       ctypes.c_double(30000)))

        i = MCS(coord=(ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0)))

        j = MCS(coord=(ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0),
                       ctypes.c_double(0)))
        k = self._Dll_InverseKinematic(ctypes.pointer(h), ctypes.pointer(i), ctypes.pointer(j))
        # f = -228990.0
        # print( d.coord[ 0 ] )
        print(h.coord[0], h.coord[1], h.coord[2], h.coord[3], h.coord[4])
        print(i.coord[0], i.coord[1], i.coord[2], i.coord[3], i.coord[4])
        print(j.coord[0], j.coord[1], j.coord[2], j.coord[3], j.coord[4])
        return i
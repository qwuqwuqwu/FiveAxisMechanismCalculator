from ctypes import *

class MCS( Structure ):
    _fields_ = [ ( "coord", c_double * 5 ) ]

class BCS( Structure ):
    _fields_ = [ ( "coord", c_double * 5 ) ]

class MyKinematicParam( Structure ):
    _fields_ = [ ( "nKinematicType", c_long ),
                 ( "nToolAxisDirection", c_long ),
                 ( "nRA", c_long ),
                 ( "nRB", c_long ),
                 ( "nAxisDirection_First", c_long ),
                 ( "nAxisDirection_Second", c_long ),
                 ( "nRotationDirection_First", c_long ),
                 ( "nRotationDirection_Second", c_long ),
                 ( "nRestrict_First", c_long * 2 ),
                 ( "nRestrict_Second", c_long * 2 ),
                 ( "nToolHolderLength", c_long ),
                 ( "nRotationOffset_First", c_long * 3 ),
                 ( "nRotationOffset_Second", c_long * 3 ),
                 ( "nPr3021to3023", c_long * 3 ),
                 ( "nPr3024to3026", c_long * 3 ),
                 ( "nPr3031to3033", c_long * 3 ),
                 ( "nPr3034to3036", c_long * 3 ),
                 ( "nPr3041to3043", c_long * 3 ),
                 ("nPr3044to3046", c_long * 3),
                 ( "nIntMode", c_long ),
                 ( "nTableCrdMode", c_long ),
                 ( "nPr3056", c_long ),
                 ( "nToolLength", c_long ),
                 ( "G54Offset", c_long * 5 )
                 ]
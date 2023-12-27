from agi.stk12.stkdesktop import STKDesktop
from agi.stk12.stkobjects import *
from agi.stk12.stkutil import *
from agi.stk12.vgt import *

import os

stk = STKDesktop.AttachToApplication ()
root = stk.Root
print ( root )

scenario = root.CurrentScenario
scenario.SetTimePeriod ( 'Today' , '+24hr' )
root.Rewind ()

target = AgTarget ( scenario.Children.New ( AgESTKObjectType.eTarget , "GroundTarget" ) )
target.Position.AssignGeodetic ( 50 ,-100 , 0 )
satellite = AgSatellite ( root.CurrentScenario.Children.New ( AgESTKObjectType.eSatellite , "LeoSat" ) )
print ( scenario.StartTime )
print ( scenario.StopTime )
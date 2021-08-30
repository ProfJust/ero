% goto_beer.m
%  ---------------------------
% EMR am 3.5.2021
%-----------------------------
% Gazebo-youBot faehrt zum Bier in leerer Welt
% $ roslaunch emr_youbot youbot_emr_simulation_empty_gazebo.launch 
% Ergänze Bierdose http://models.gazebosim.org/Beer vor dem youbot
% Abstand max.  5,6 m
%------------------------------------------------------------------------
ROS_Node_init_localhost;

%% --- Subscriber und Publisher beim Master anmelden
sub1 = rossubscriber('summit_xl/front_laser/scan','sensor_msgs/LaserScan');
pub1 = rospublisher ('cmd_vel', 'geometry_msgs/Twist');
msgsVel = rosmessage(pub1); % zunächst leere Msg

%% --- Plot vorbereiten ------
close all;
figure;

%% 1mal Scan-Daten holen
scandata = receive(sub1,10); % Abstandswerte holen
% Zeilenzahl der 1. Spalte ermitteln
numbOfScans = size(scandata.Ranges,1);
% Winkelbereich ermitteln
minAngle = scandata.AngleMin;
maxAngle = scandata.AngleMax;
% Im Laserscan sind nur Abstände, aber keine Winkel =>
% Winkelvektor mit gleicher Spaltenzahl erstellen
% angles = (minAngle: (maxAngle-minAngle)/(numbOfScans-1): maxAngle);
angles = (minAngle: scandata.AngleIncrement: maxAngle);

%% --- Loop() -----
go = true; % Loop-Flag
while go    
    scandata = receive(sub1,10); 
    polarplot(angles,scandata.Ranges,'.');
    % Begrenzung der Angezeigten Reichweite = Radius r    
    rlim([0 scandata.RangeMax]);
    % Begrenzung der Anzeige auf Winkelbereich [min max ]    
    thetalim([scandata.AngleMin*180/pi scandata.AngleMax*180/pi]);
    % Textausgabe Abstand
    disp(scandata.Ranges(numbOfScans/2));  % direkt nach vorn
    
    %% Suche Kleinsten Abstandswert => Winkel to go
    minIndex = 1; % Index 0 nicht existen!!!  
    minRange = scandata.Ranges(minIndex); 
    for i=1:1:numbOfScans
        if scandata.Ranges(i) < minRange            
            minIndex = i;            
            minRange = scandata.Ranges(minIndex);
        end
    end
    disp(minIndex)    
    disp(minRange)
    
    %% Bis auf 10cm heranfahren
    if minRange>0.10 %10cm   
        if(minRange>1)
            msgsVel.Linear.X = 0.5;
        else
            msgsVel.Linear.X = 0.2;
        end
        disp('GO');
        % Querfahrt
        if minIndex > numbOfScans/2 + 4         
            msgsVel.Linear.Y=0.5; %Go left            
            disp('LEFT');
        end
        if minIndex < numbOfScans/2 -4  
            msgsVel.Linear.Y=-0.5;%Go right             
            disp('RIGHT');
        end       
        
    else %STOP          
        disp('STOP');        
        msgsVel.Linear.X=0.0;        
        msgsVel.Linear.Y=0.0;        
        go = false;
    end
    
    send(pub1,msgsVel);    
    pause(0.2);   
end
pause(10);
close all;


clear all
close all
set(0,'DefaultFigureWindowStyle','docked')
clc

Data = xlsread('APDL_all.xlsx');

%% résistance
APDL_R = Data([1:10],[1]);
S1_R = Data([1:8],[3]);
S2_R = Data([1:8],[5]);
ED1_R = Data(:,[7]);
ED2_R = Data(:,[9]);
Woven_R = Data([1:10],11);
strength = [APDL_R; Woven_R; S1_R; S2_R; ED1_R; ED2_R];

g1 = repmat({'APDL UD'},10,1);
g2 = repmat({'APDL Woven'},10,1);
g3 = repmat({'S1 (25.4x12.7)'},8,1);
g4 = repmat({'S2 (12.7x3.175)'},8,1);
g5 = repmat({'ED1'},32,1);
g6 = repmat({'ED2'},32,1);

g = [g1;g2;g3;g4;g5;g6];

figure(1)
boxplot(strength,g)
ylabel('Résistance (MPa)')


%% module
APDL_E = Data((1:10),[2]); %#ok<*NBRAK>
S1_E = Data([1:8],[4]);
S2_E = Data([1:8],[6]);
ED1_E = Data(:,[8]);
ED2_E = Data(:,[10]);
Woven_E = Data([1:10],12);
Module = [APDL_E; Woven_E; S1_E; S2_E; ED1_E; ED2_E];

figure(2)
boxplot(Module,g);
ylabel('Module (GPa)')

%% stress strain

% UD chips
SS = xlsread('APDL_StressStrain.xlsx');

E1 = SS(:,(1:3));
E2 = SS(:,(4:6));
E3 = SS(:,(7:9));
E4 = SS(:,(10:12));
E5 = SS(:,(13:15));
E6 = SS(:,(16:18));
E7 = SS(:,(19:21));
E8 = SS(:,(22:24));
E9 = SS(:,(25:27));
E10 = SS(:,(28:30));

figure(3)
subplot(2,1,1);
hold on
plot(E1(:,3),E1(:,2))
plot(E2(:,3),E2(:,2))
plot(E3(:,3),E3(:,2))
plot(E4(:,3),E4(:,2))
plot(E5(:,3),E5(:,2))
plot(E6(:,3),E6(:,2))
plot(E7(:,3),E7(:,2))
plot(E8(:,3),E8(:,2))
plot(E9(:,3),E9(:,2))
plot(E10(:,3),E10(:,2))

xlabel('Displacement (mm)')
ylabel('Macro-Stress (MPa)')
title('APDL UD chips')
% legend('Specimen 1',...
%     'Specimen 2',...
%     'Specimen 3',...
%     'Specimen 4',...
%     'Specimen 5',...
%     'Specimen 6',...
%     'Specimen 7',...
%     'Specimen 8',...
%     'Specimen 9',...
%     'Specimen 10')

hold off

% Woven chips
WSS = xlsread('APDL_Woven_SS.xlsx');

E1W = WSS(:,(1:3));
E2W = WSS(:,(4:6));
E3W = WSS(:,(7:9));
E4W = WSS(:,(10:12));
E5W = WSS(:,(13:15));
E6W = WSS(:,(16:18));
E7W = WSS(:,(19:21));
E8W = WSS(:,(22:24));
E9W = WSS(:,(25:27));
E10W = WSS(:,(28:30));

subplot(2,1,2);
hold on
plot(E1W(:,3),E1W(:,2))
plot(E2W(:,3),E2W(:,2))
plot(E3W(:,3),E3W(:,2))
plot(E4W(:,3),E4W(:,2))
plot(E5W(:,3),E5W(:,2))
plot(E6W(:,3),E6W(:,2))
plot(E7W(:,3),E7W(:,2))
plot(E8W(:,3),E8W(:,2))
plot(E9W(:,3),E9W(:,2))
plot(E10W(:,3),E10W(:,2))

xlabel('Displacement (mm)')
ylabel('Macro-Stress (MPa)')
title('APDL Woven chips')
% legend('Specimen 1',...
%     'Specimen 2',...
%     'Specimen 3',...
%     'Specimen 4',...
%     'Specimen 5',...
%     'Specimen 6',...
%     'Specimen 7',...
%     'Specimen 8',...
%     'Specimen 9',...
%     'Specimen 10')

hold off







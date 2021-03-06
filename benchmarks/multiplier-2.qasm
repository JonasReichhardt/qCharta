OPENQASM 2.0;
include "qelib1.inc";
qreg a[2];
qreg b[2];
qreg out[4];
creg meas[8];
rz(45*pi/32) b[0];
rz(45*pi/16) b[1];
rz(pi/2) out[3];
sx out[3];
rz(15*pi/16) out[3];
cx out[3],out[2];
rz(-pi/4) out[2];
cx out[3],out[2];
rz(3*pi/4) out[2];
sx out[2];
rz(7*pi/8) out[2];
cx out[3],out[1];
rz(-pi/8) out[1];
cx out[3],out[1];
rz(pi/8) out[1];
cx out[2],out[1];
rz(-pi/4) out[1];
cx out[2],out[1];
rz(3*pi/4) out[1];
sx out[1];
rz(3*pi/4) out[1];
cx out[3],out[0];
rz(-pi/16) out[0];
cx out[3],out[0];
rz(pi/16) out[0];
cx out[2],out[0];
rz(-pi/8) out[0];
cx out[2],out[0];
rz(pi/8) out[0];
cx out[1],out[0];
rz(-pi/4) out[0];
cx out[1],out[0];
rz(3*pi/4) out[0];
sx out[0];
rz(pi/2) out[0];
cx b[1],out[0];
rz(-pi) out[0];
cx b[1],out[0];
cx b[1],a[1];
rz(-pi) a[1];
rz(pi) out[0];
cx a[1],out[0];
rz(pi) out[0];
cx a[1],out[0];
cx b[1],a[1];
rz(pi) a[1];
cx b[1],out[1];
rz(-pi) out[0];
cx a[1],out[0];
rz(-pi) out[0];
cx a[1],out[0];
rz(pi) out[0];
cx b[0],out[0];
rz(-pi/2) out[0];
cx b[0],out[0];
rz(pi/2) out[0];
rz(-pi/2) out[1];
cx b[1],out[1];
cx b[1],a[1];
rz(-pi/2) a[1];
rz(pi/2) out[1];
cx a[1],out[1];
rz(pi/2) out[1];
cx a[1],out[1];
cx b[1],a[1];
rz(pi/2) a[1];
cx b[1],out[2];
rz(-pi/2) out[1];
cx a[1],out[1];
rz(-pi/2) out[1];
cx a[1],out[1];
rz(pi/2) out[1];
rz(-pi/4) out[2];
cx b[1],out[2];
cx b[1],a[1];
rz(-pi/4) a[1];
rz(pi/4) out[2];
cx a[1],out[2];
rz(pi/4) out[2];
cx a[1],out[2];
cx b[1],a[1];
rz(pi/4) a[1];
cx b[1],out[3];
rz(-pi/4) out[2];
cx a[1],out[2];
rz(-pi/4) out[2];
cx a[1],out[2];
rz(pi/4) out[2];
rz(-pi/8) out[3];
cx b[1],out[3];
cx b[1],a[1];
rz(-pi/8) a[1];
rz(pi/8) out[3];
cx a[1],out[3];
rz(pi/8) out[3];
cx a[1],out[3];
cx b[1],a[1];
rz(pi/8) a[1];
rz(-pi/8) out[3];
cx a[1],out[3];
rz(-pi/8) out[3];
cx a[1],out[3];
cx b[0],a[1];
rz(-pi/2) a[1];
cx a[1],out[0];
rz(pi/2) out[0];
cx a[1],out[0];
cx b[0],a[1];
rz(pi/2) a[1];
cx b[0],out[1];
rz(-pi/2) out[0];
cx a[1],out[0];
rz(-pi/2) out[0];
cx a[1],out[0];
rz(pi/2) out[0];
cx b[1],out[0];
rz(-pi/2) out[0];
cx b[1],out[0];
cx b[1],a[0];
rz(-pi/2) a[0];
rz(pi/2) out[0];
cx a[0],out[0];
rz(pi/2) out[0];
cx a[0],out[0];
cx b[1],a[0];
rz(pi/2) a[0];
rz(-pi/2) out[0];
cx a[0],out[0];
rz(-pi/2) out[0];
cx a[0],out[0];
rz(pi/2) out[0];
rz(-pi/4) out[1];
cx b[0],out[1];
cx b[0],a[1];
rz(-pi/4) a[1];
rz(pi/4) out[1];
cx a[1],out[1];
rz(pi/4) out[1];
cx a[1],out[1];
cx b[0],a[1];
rz(pi/4) a[1];
cx b[0],out[2];
rz(-pi/4) out[1];
cx a[1],out[1];
rz(-pi/4) out[1];
cx a[1],out[1];
rz(pi/4) out[1];
cx b[1],out[1];
rz(-pi/4) out[1];
cx b[1],out[1];
cx b[1],a[0];
rz(-pi/4) a[0];
rz(pi/4) out[1];
cx a[0],out[1];
rz(pi/4) out[1];
cx a[0],out[1];
cx b[1],a[0];
rz(pi/4) a[0];
rz(-pi/4) out[1];
cx a[0],out[1];
rz(-pi/4) out[1];
cx a[0],out[1];
rz(pi/4) out[1];
rz(-pi/8) out[2];
cx b[0],out[2];
cx b[0],a[1];
rz(-pi/8) a[1];
rz(pi/8) out[2];
cx a[1],out[2];
rz(pi/8) out[2];
cx a[1],out[2];
cx b[0],a[1];
rz(pi/8) a[1];
rz(-pi/8) out[2];
cx a[1],out[2];
rz(-pi/8) out[2];
cx a[1],out[2];
rz(pi/8) out[2];
cx b[1],out[2];
rz(-pi/8) out[2];
cx b[1],out[2];
cx b[1],a[0];
rz(-pi/8) a[0];
rz(pi/8) out[2];
cx a[0],out[2];
rz(pi/8) out[2];
cx a[0],out[2];
cx b[1],a[0];
rz(pi/8) a[0];
rz(-pi/8) out[2];
cx a[0],out[2];
rz(-pi/8) out[2];
cx a[0],out[2];
rz(pi/8) out[2];
rz(pi/8) out[3];
cx b[0],out[3];
rz(-pi/16) out[3];
cx b[0],out[3];
cx b[0],a[1];
rz(-pi/16) a[1];
rz(pi/16) out[3];
cx a[1],out[3];
rz(pi/16) out[3];
cx a[1],out[3];
cx b[0],a[1];
rz(pi/16) a[1];
cx b[0],out[0];
rz(-pi/4) out[0];
cx b[0],out[0];
rz(pi/4) out[0];
rz(-pi/16) out[3];
cx a[1],out[3];
rz(-pi/16) out[3];
cx a[1],out[3];
rz(pi/16) out[3];
cx b[1],out[3];
rz(-pi/16) out[3];
cx b[1],out[3];
cx b[1],a[0];
rz(-pi/16) a[0];
rz(pi/16) out[3];
cx a[0],out[3];
rz(pi/16) out[3];
cx a[0],out[3];
cx b[1],a[0];
rz(pi/16) a[0];
rz(-pi/16) out[3];
cx a[0],out[3];
rz(-pi/16) out[3];
cx a[0],out[3];
cx b[0],a[0];
rz(-pi/4) a[0];
cx a[0],out[0];
rz(pi/4) out[0];
cx a[0],out[0];
cx b[0],a[0];
rz(pi/4) a[0];
cx b[0],out[1];
rz(-pi/4) out[0];
cx a[0],out[0];
rz(-pi/4) out[0];
cx a[0],out[0];
rz(3*pi/4) out[0];
sx out[0];
rz(pi/2) out[0];
rz(-pi/8) out[1];
cx b[0],out[1];
cx b[0],a[0];
rz(-pi/8) a[0];
rz(pi/8) out[1];
cx a[0],out[1];
rz(pi/8) out[1];
cx a[0],out[1];
cx b[0],a[0];
rz(pi/8) a[0];
cx b[0],out[2];
rz(-pi/8) out[1];
cx a[0],out[1];
rz(-pi/8) out[1];
cx a[0],out[1];
rz(3*pi/8) out[1];
cx out[1],out[0];
rz(pi/4) out[0];
cx out[1],out[0];
rz(-pi/4) out[0];
sx out[1];
rz(pi/2) out[1];
rz(-pi/16) out[2];
cx b[0],out[2];
cx b[0],a[0];
rz(-pi/16) a[0];
rz(pi/16) out[2];
cx a[0],out[2];
rz(pi/16) out[2];
cx a[0],out[2];
cx b[0],a[0];
rz(pi/16) a[0];
rz(-pi/16) out[2];
cx a[0],out[2];
rz(-pi/16) out[2];
cx a[0],out[2];
rz(3*pi/16) out[2];
cx out[2],out[0];
rz(pi/8) out[0];
cx out[2],out[0];
rz(-pi/8) out[0];
cx out[2],out[1];
rz(pi/4) out[1];
cx out[2],out[1];
rz(-pi/4) out[1];
sx out[2];
rz(pi/2) out[2];
rz(pi/16) out[3];
cx b[0],out[3];
rz(-1*pi/32) out[3];
cx b[0],out[3];
cx b[0],a[0];
rz(-1*pi/32) a[0];
rz(1*pi/32) out[3];
cx a[0],out[3];
rz(1*pi/32) out[3];
cx a[0],out[3];
cx b[0],a[0];
rz(1*pi/32) a[0];
rz(-1*pi/32) out[3];
cx a[0],out[3];
rz(-1*pi/32) out[3];
cx a[0],out[3];
rz(3*pi/32) out[3];
cx out[3],out[0];
rz(pi/16) out[0];
cx out[3],out[0];
rz(-pi/16) out[0];
cx out[3],out[1];
rz(pi/8) out[1];
cx out[3],out[1];
rz(-pi/8) out[1];
cx out[3],out[2];
rz(pi/4) out[2];
cx out[3],out[2];
rz(-pi/4) out[2];
sx out[3];
rz(pi/2) out[3];
barrier a[0],a[1],b[0],b[1],out[0],out[1],out[2],out[3];
measure a[0] -> meas[0];
measure a[1] -> meas[1];
measure b[0] -> meas[2];
measure b[1] -> meas[3];
measure out[0] -> meas[4];
measure out[1] -> meas[5];
measure out[2] -> meas[6];
measure out[3] -> meas[7];

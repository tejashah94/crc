import os
from subprocess import Popen
INPUT_PATH="/home/hemanth/btp/code2/crc/ChampSim_CRC2/input/";
BIN_PATH="/home/hemanth/btp/code2/crc/ChampSim_CRC2/bin/";
TRACE_PATH="/home/hemanth/btp/code2/crc/ChampSim_CRC2/trace/";
OUTPUT_PATH="/home/hemanth/btp/code2/crc/ChampSim_CRC2/output/";
ERR_PATH="/home/hemanth/btp/code2/crc/ChampSim_CRC2/err/";
waitObjects=[];
outObjects=[];
errObjects=[];
inObjects=[];
files = os.listdir(INPUT_PATH);

count=0;
def waitForFinish():
	global waitObjects, outObjects, errObjects, inObjects
	for i in range(len(waitObjects)):
		waitObjects[i].wait();
		outObjects[i].close();
		errObjects[i].close();
		inObjects[i].close();
	waitObjects=[];
	outObjects=[];
	errObjects=[];
	inObjects=[];

for file in files:
	count = count+1;
	print file+"\n";
	print "count: "+str(count)+"\n";
	inFO = open(INPUT_PATH+file, "r");
	outFO = open(OUTPUT_PATH+"out_"+file, "w");
	errFO = open(ERR_PATH+"err_"+file, "w");
	wo = Popen([BIN_PATH+"srrip-positioned-config1", "-simulation_instructions", "10000000", "-traces", TRACE_PATH+"libquantum_10M.trace.gz"], stdin=inFO, stdout=outFO, stderr=errFO);
	waitObjects.append(wo);
	outObjects.append(outFO);
	errObjects.append(errFO);
	inObjects.append(inFO);
	if count==32:
		waitForFinish();
		count=0;



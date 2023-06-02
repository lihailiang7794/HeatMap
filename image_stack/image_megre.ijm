
var recording_time=24;
var q=recording_time+1;

save_path="D:/desk/image_stack/output/";
temporary_save_path="D:/desk/image_stack/output1/";

data_fold="test"



run("8-bit");
run("Stack Splitter", "number="+recording_time);

selectWindow(data_fold);
close();

for(j=1;j<q;j++){

filepath=save_path;
if (j<9){
	selectWindow("stk_000"+j+"_"+data_fold);
run("Z Project...", "projection=[Standard Deviation]");
saveAs("Jpeg", filepath+"MED_stk_000"+j+"_"+data_fold+".jpg");
close();
}


if (j==9){
selectWindow("stk_000"+j+"_"+data_fold);
run("Z Project...", "projection=[Standard Deviation]");
saveAs("Jpeg", filepath+"MED_stk_000"+j+"_"+data_fold+".jpg");
close();
}


	
if (j>9){
	selectWindow("stk_00"+j+"_"+data_fold);
run("Z Project...", "projection=[Standard Deviation]");
saveAs("Jpeg", filepath+"MED_stk_00"+j+"_"+data_fold+".tif");
close();
}

close();
}






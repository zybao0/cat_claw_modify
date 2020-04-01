if(typeof localStorage['Ext']==='undefined' || localStorage['Ext'] == ''){
    var Ext = new Array(
        {"ext":"flv","size":10},
        {"ext":"hlv","size":10},
        {"ext":"f4v","size":10},
        {"ext":"mp4","size":10},
        {"ext":"mp3","size":10},
        {"ext":"wma","size":10},
        {"ext":"wav","size":10},
        {"ext":"m4a","size":10},
        {"ext":"letv","size":10},
        {"ext":"ts","size":10},
        {"ext":"webm","size":10},
        {"ext":"ogg","size":10},
        {"ext":"ogv","size":10},
        {"ext":"acc","size":10},
        {"ext":"mov","size":10},
        {"ext":"mkv","size":10},
        {"ext":"m3u8","size":0}
    );
    localStorage['Ext'] = JSON.stringify(Ext);
}
// if(typeof localStorage['m3u8DownloadServer']==='undefined'||localStorage['m3u8DownloadServer']==''){
//     var m3u8DownloadServer = new Array(
//         {"IP":"127.0.0.1"},
//         {"FileName":"download.py"},
//         {"Port":8888},
//     );
//     localStorage['m3u8DownloadServer'] = JSON.stringify(m3u8DownloadServer);
// }
if(typeof localStorage['Type']==='undefined'){
    var Type = new Array(
        {"Type":"video/*"},
        {"Type":"audio/*"}
    );
    localStorage['Type'] = JSON.stringify(Type);
}

if(typeof localStorage['repeat']==='undefined'){
    localStorage['repeat'] = true;
}

if(typeof localStorage['repeatReg']==='undefined'){
    localStorage['repeatReg'] = "\\?[\\S]+";
}

if(typeof localStorage['Debug']==='undefined'){
    localStorage['Debug'] = true;
}

if(typeof localStorage['TitleName']==='undefined'){
    localStorage['TitleName'] = true;
}

if(typeof localStorage['m3u8DownloadServer_ip']==='undefined'){
    localStorage['m3u8DownloadServer_ip'] = "127.0.0.1";
}

if(typeof localStorage['m3u8DownloadServer_file']==='undefined'){
    localStorage['m3u8DownloadServer_file'] = "download.py";
}

if(typeof localStorage['m3u8DownloadServer_port']==='undefined'){
    localStorage['m3u8DownloadServer_port'] = 8888;
}
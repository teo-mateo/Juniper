// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

chrome.browserAction.onClicked.addListener(function(tab) {
    /*
    var req = new XMLHttpRequest();
    req.open("GET", "http://bardici.ro/section/links/addlink/", false);
    req.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    req.send("csrfmiddlewaretoken=cI1YkCpPwSS67mDNASt9lhHM09iG8ear&link=" + encodeURIComponent(tab.url));
    */

    //var sendto = "http://bardici.ro/blog/section/links/addlink/";
    var sendto = "http://127.0.0.1:8000/section/links/addlink/";


    $.get(
        sendto,
        {
            "security_token": "4df52be1-5f8e-4c1b-9205-6a83fecf7ed1",
            "link": tab.url,
            "title": tab.title,
            "tags": "tagone,tagtwo"
        },
        function(data){}
    );
});

function createRequest(){
    var result = null;
    result = new XMLHttpRequest();
    return result;
}
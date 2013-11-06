// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

chrome.browserAction.onClicked.addListener(function(tab) {
    var req = new XMLHttpRequest();
    req.open("POST", "http://127.0.0.1:8000/section/links/addlink/", false);
    req.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    req.send("csrfmiddlewaretoken=cI1YkCpPwSS67mDNASt9lhHM09iG8ear&link=" + encodeURIComponent(tab.url));
});

function createRequest(){
    var result = null;
    result = new XMLHttpRequest();
    return result;
}
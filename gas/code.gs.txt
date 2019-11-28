/**
 * @OnlyCurrentDoc
 */

function doPost(e) {
  // Controller
  if (e.parameter.team_id) {
    returnSlackReply(e);
    writeBotLog(e);
  } else if (e.parameter.pi_id) {
    writeAireLog(e);
  }
}



function writeAireLog(e) {
  var time_stamp = e.parameter.timestamp;
  var pi_id = e.parameter.pi_id;
  var temperature = e.parameter.temperature;
  var humidity = e.parameter.humidity;
  
  var paramNameList = ["time_stamp", "pi_id", "temperature", "humidity"];
  var paramList = [time_stamp, pi_id, temperature, humidity];
  
  var ss = SpreadsheetApp.getActiveSpreadsheet(); // スプレッドシートオブジェクトを取得
  var sheet = ss.getSheetByName("air_condition"); // シートを指定
  var lastRow = sheet.getLastRow();
  
  // 行名が設定されていない場合は設定する
  if(lastRow < 1)　{
    for(var i=0; i<paramNameList.length; i++) {
      sheet.getRange(1, i+1).setValue(paramNameList[i]);
    }
    lastRow = 1;
  }
  
  // 値をセット
  for(var i=0; i<paramList.length; i++) {
      sheet.getRange(lastRow+1, i+1).setValue(paramList[i]);
  }
}


function returnSlackReply(e) {
  var get_text = e.parameter.text.substr(4);
  var reply = "受け取ったぞ:" + get_text;
  var options =
  {
    "method" : "post",
    "contentType" : "application/json",
    "payload" : JSON.stringify(
      {
        "text" : reply,
      }
    )
  };
  UrlFetchApp.fetch("https://hooks.slack.com/services/?????????/?????????/????????????????????????", options);
}

function writeBotLog(e) {
  var time_stamp = e.parameter.timestamp;
  var team_id = e.parameter.team_id;
  var team_domain = e.parameter.team_domain;
  var channel_id = e.parameter.channel_id;
  var channel_name = e.parameter.channel_name;
  var user_id = e.parameter.user_id;
  var user_name = e.parameter.user_name;
  var msg = e.parameter.text;
  
  var paramNameList = ["time_stamp", "team_id", "team_domain", "channel_id", "channel_name", "user_id", "user_name", "msg"];
  var paramList = [time_stamp, team_id, team_domain, channel_id, channel_name, user_id, user_name, msg];
  
  var ss = SpreadsheetApp.getActiveSpreadsheet(); // スプレッドシートオブジェクトを取得
  var sheet = ss.getSheetByName("log"); // シートを指定
  var lastRow = sheet.getLastRow();
  
  // 行名が設定されていない場合は設定する
  if(lastRow < 1)　{
    for(var i=0; i<paramNameList.length; i++) {
      sheet.getRange(1, i+1).setValue(paramNameList[i]);
    }
    lastRow = 1;
  }
  
  // 値をセット
  for(var i=0; i<paramList.length; i++) {
      sheet.getRange(lastRow+1, i+1).setValue(paramList[i]);
  }
}

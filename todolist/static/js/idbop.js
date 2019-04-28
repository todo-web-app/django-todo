var dbPromise = idb.open('todo-db', 1, function(upgradeDb) {
    upgradeDb.createObjectStore('todos',{keyPath:'pk'});
});

//collect latest post from server and store in idb
fetch('http://127.0.0.1:8000/getdata').then(function(response){
    return response.json();
}).then(function(jsondata){
    dbPromise.then(function(db){
        var tx = db.transaction('todos', 'readwrite');
          var todosStore = tx.objectStore('todos');
          for(var key in jsondata){
              if (jsondata.hasOwnProperty(key)) {
                todosStore.put(jsondata[key]);	
              }
          }
    });
});

//retrive data from idb and display on page
var todos = "";
dbPromise.then(function(db){
    var tx = db.transaction('todos', 'readonly');
    var feedsStore = tx.objectStore('todos');
    return feedsStore.openCursor();
}).then(function logItems(cursor) {
        if (!cursor) {
        document.getElementById('todos').innerHTML=todos;
        return;
        }
        for (var field in cursor.value) {
            if(field=='fields'){
                feedsData=cursor.value[field];
                console.log(feedsData);
                for(var key in feedsData){
                    if(key =='title'){
                        var title = feedsData[key];
                    }
                }
                todos = todos+'<li class="list-group-item">'+title+'</li>';
                console.log(todos);
            }
        }
        return cursor.continue().then(logItems);
    });
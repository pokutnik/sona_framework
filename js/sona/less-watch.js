;(function(window, undefined){
    console.log("start watch hook");
    var cache = window.localStorage ||  null;
    var re = /^http:(.)*.less(:timestamp)?$/
    for(key in localStorage) {
         if(re.test(key)) {
             cache.removeItem(key);
         }
    } 
    var watchTimer = setInterval(function (){
        less.refresh(true);
    }, 5000);
})(window);

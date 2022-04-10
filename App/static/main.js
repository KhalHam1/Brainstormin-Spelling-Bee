
async function getUserData(){
    const response = await fetch('/api/users');
    return response.json();
}

function loadTable(users){
    const table = document.querySelector('#result');
    for(let user of users){
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}
function remove_from_start(i, array){
    let j = 0;
    while(j < i){
        array.shift();
        j++;
    }
    return array;
}

function create_words_array(crazyArray){
    currWord = []
    currString = "New String";
    wordsArray = []
    i = 0;

    while (i<crazyArray.length){
        if(crazyArray[i]>='A'&&crazyArray[i]<='z'){
            currWord.push(crazyArray[i])
            currString = String(currWord);
            wordsArray.push(currString);
            currWord=[];

        }
        i++;
    }
    m=0;
    currWord=[]
    currString2="";
    wordsArray2 = [];
    while(m<wordsArray.length){
        if(wordsArray[m]>='A'&&wordsArray[m]<='Z'){
            currString2=currString2+wordsArray[m];
            n = m+1;
            while(wordsArray[n]>='a'&&wordsArray[n]<='z'){
                currString2=currString2+wordsArray[n];
                n++;
            }
            wordsArray2.push(currString2);
            currString2="";
            
        }
        m++
    }
    return wordsArray2;

}

function cleanArr(){
    var element = document.querySelector('#test');
    var temp = document.createElement("div");
    temp.appendChild( element.cloneNode( true ) );
    
    var arrayString = temp.innerHTML;
    var charArray = []
    for (i=0;i<509;i++){
        charArray.push(arrayString[i]);
    }
    temp = element = null;
    prologue = []
    
    for(i=0;i<16;i++){
        prologue.push(arrayString[i]);
        
    }
    l = arrayString.length
    let arrayString_no_prologue = remove_from_start(16, charArray);
    arrayString_no_prologue.pop();
    arrayString_no_prologue.pop();
    arrayString_no_prologue.pop();
    arrayString_no_prologue.pop();
    arrayString_no_prologue.pop();
    arrayString_no_prologue.pop();
    arrayString_no_prologue.pop();
   
    var filtered_by_commas = arrayString_no_prologue.filter(function(e) { return e !== ',' })
    var removed_whitespaces = filtered_by_commas.filter(function(str) { return /\S/.test(str);});
    string = String(arrayString);
   
    arrayString_no_prologue = removed_whitespaces;
    return arrayString_no_prologue;
}

function extractWords(){
    let arrayString = cleanArr();
    let stringified = String(arrayString);
    let array_restart= Array.from(stringified);
    let chars = []
    
    for(i=0;i<array_restart.length;i++){
        chars.push(array_restart[i]);
    }
    wordsArray = create_words_array(chars);
    let x = Math.floor((Math.random() * wordsArray.length) + 0);
    document.getElementById('test2').innerHTML = wordsArray[x];
    speakbutton();
    return wordsArray[x]; 
}

function collectWord(word){
     document.getElementById('test2').innerHTML = word;
    console.log("Collected word: " + typeof(word))
}

function speakbutton(){
   word = document.getElementById('test2');
   var element = document.querySelector('#test2');
   var temp = document.createElement("div");
   temp.appendChild( element.cloneNode( true ) );
    
   var arrayString = temp.innerHTML;
   
   temp = element = null;
   
   
   var charArray = []
   for (i=0;i<arrayString.length;i++){
       charArray.push(arrayString[i]);
   }
   let arrayString_no_prologue = remove_from_start(16, charArray);
   let m = arrayString_no_prologue.length-1;
   while(arrayString_no_prologue[m]!='<'){
       arrayString_no_prologue.pop();
       m=m-1;
   }
   
   wordToSpeak = create_words_array(charArray);
   stringified = String(wordToSpeak);
   console.log('Final Word to Speak: ' + stringified);
   console.log('Final Word Type: ' + typeof(stringified));
   let utter = new SpeechSynthesisUtterance();
   utter.lang = 'en-US';
   if (wordToSpeak == ""){
       utter.text = "Please generate a word."
   }
   else{
       utter.text = wordToSpeak;
   }
   utter.volume = 2;
   utter.rate = 0.45;
   window.speechSynthesis.speak(utter)
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

main();
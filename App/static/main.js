
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
    // arrayString_no_prologue2 = String(arrayString_no_prologue);
    // arrayString_no_prologue2.replace(/,/g, '');
    var filtered_by_commas = arrayString_no_prologue.filter(function(e) { return e !== ',' })
    var removed_whitespaces = filtered_by_commas.filter(function(str) { return /\S/.test(str);});
    string = String(arrayString);
    // console.log(arrayString);
    // console.log('Length of arrayString: '+l);
    // console.log('Type of arrayString: '+typeof(arrayString));
    // console.log('Prologue :'+prologue);
    // console.log('arrayString_Prologue Removed: '+arrayString_no_prologue);
    // console.log('arrayString_removed_commas: '+filtered_by_commas);
    // console.log('arrayString_updated: '+removed_whitespaces);
    arrayString_no_prologue = removed_whitespaces;
    // console.log('updated_length: '+arrayString_no_prologue.length);
    return arrayString_no_prologue;
}

function extractWords(){
    let arrayString = cleanArr();
    let stringified = String(arrayString);
    console.log('Current Type: '+ typeof(stringified));
    console.log('Length of String: '+ stringified.length)
    console.log('Pre-Extraction Body: '+ stringified);
    let array_restart= Array.from(stringified);
    console.log('New Type: '+ typeof(array_restart));
    console.log('New Length: '+ array_restart.length);
    let chars = []
    
    for(i=0;i<array_restart.length;i++){
        chars.push(array_restart[i]);
    }
    console.log('Origins: '+ chars);
    // let project_reduction = array_restart.filter(function(e) { return e !== ',' })
    // console.log('Project Reduction Engaged: '+ project_reduction);
    
}

async function main(){
    const users = await getUserData();
    loadTable(users);
}

main();
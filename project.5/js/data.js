

const txt = "C++"
let i = 0;

function dawera(){
    if (i < txt.length) {
        document.getElementById("typing").innerHTML += txt.charAt
        (i);
        i++;
        setTimeout(dawera, 90)
    }

}

dawera();
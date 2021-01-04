/**
    정확성: 50.0
    효율성: 0.0
    합계: 50.0 / 100.0
 */
function test1(participant, completion) {
    var answer = '';

    for(var i=0; i<completion.length; i++){
        participant.splice(participant.indexOf(completion[i]),1);
    }

    answer = participant[0];

    return answer;
}

//정답
function solution(participant, completion) {
    participant.sort();
    completion.sort();

    for(var i=0; i<completion.length; i++){
        if(completion[i] != participant[i]){
            return participant[i];
        }
    }

    return participant[participant.length-1];
}

a = solution(["leo", "kiki", "eden"],["eden", "kiki"]); // 결과: leo
b = solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]); // 결과: vinko
c = solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]); // 결과: mislav

console.log(a);
console.log(b);
console.log(c);
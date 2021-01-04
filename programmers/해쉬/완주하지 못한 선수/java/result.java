package result;

import java.util.*;

public class result {
	public static String solution(String[] participant, String[] completion) {
		String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        for (String player : participant) hm.put(player, hm.getOrDefault(player, 0) + 1);
        for (String player : completion) hm.put(player, hm.get(player) - 1);

        System.out.println(hm);
        
        for (String key : hm.keySet()) {
            if (hm.get(key) != 0){
                answer = key;
            }
        }
        return answer;
    }
	
	public static void main(String[] args) {
		String a = solution(new String[] {"leo", "kiki", "eden"},new String[] {"eden", "kiki"});
		String b = solution(new String[] {"marina", "josipa", "nikola", "vinko", "filipa"},new String[] {"josipa", "filipa", "marina", "nikola"});
		String c = solution(new String[] {"mislav", "stanko", "mislav", "ana"},new String[] {"stanko", "ana", "mislav"});
		
		System.out.println(a); // 결과: leo
		System.out.println(b); // 결과: vinko
		System.out.println(c); // 결과: mislav
	}
}

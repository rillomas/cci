
public class IsRotation {
	public static void main(String[] args) {
		boolean ok = isRotation("waterbottle", "erbottlewat");
		if (ok) {
			System.out.println("OK!");
		} else {
			System.out.println("Not OK...");
		}
	}
		
	private static boolean isSubstring(String s1, String s2) {
		return s2.contains(s1);
	}
	
	private static boolean isRotation(String s1, String s2) {
		if (s1 == null || s2 == null) {
			throw new IllegalArgumentException("s1 and s2 must not be null");
		}
		
		if (s1.length() == s2.length()) {
			String concat = s1 + s1;
			return isSubstring(s2, concat);
		}
		return false;
	}
}

public class App {
    public static void main(String[] args) throws Exception {
        class solution {
            public static int function1(int a, int b, int c) {
              return a + b * c ;
            }
            
            public static int function2(int a, int b, int c) {
              return (a+b)%c ;
            }
            
            public static int function3(int a, int b, int c) {
              return c - b * (c/a);
            }
            
            public static int function4(int a, int b, int c) {
              return (c*a-b)/(b%c)+b;
            }
            public static float celsius2fahrenheit(int temp) {
                return (temp * 9.0f / 5.0f) + 32;
            }
            public static String pig_latin(String first, String last) {
                int fLen = first.length();
                int lLen = last.length();
                String newFirst = 
                first.substring(1, 2).toUpperCase()
                + first.substring(2, fLen)
                + first.substring(0, 1)
                + "ay";
                String newLast = 
                last.substring(1, 2).toUpperCase()
                + last.substring(2, lLen)
                + last.substring(0, 1)
                + "ay";
                return newFirst + " " + newLast ;
            }
          }
        
          solution sol = new solution();
          int a = 5, b=10, c=3;
          int a1 = sol.function1(a, b, c);
          int a2 = sol.function2(a, b, c);
          int a3 = sol.function3(a, b, c);
          int a4 = sol.function4(a, b, c);
          System.out.println(a1);
          System.out.println(a2);
          System.out.println(a3);
          System.out.println(a4);

          String first_name = "walt";
          String last_name = "savitch";
          System.out.println(sol.pig_latin(first_name, last_name));
    }
}

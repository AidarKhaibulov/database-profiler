public class Outer {
    private int x;
    private static String s;

    static class StaticNested{
        private int y;

        public void doSmth(){
            System.out.println(s);
            System.out.println(y);
        }

    }

     class Inner{
        private int y;

        public void doSmth(){
            System.out.println(s);
            System.out.println(y);
        }
    }
    public void print(){
        class Logger{
            public void pp(){
                System.out.println(Logger.class);
            }
        }
        Logger l= new Logger();
        l.pp();
    }
}

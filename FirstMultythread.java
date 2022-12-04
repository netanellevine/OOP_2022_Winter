public class FirstMultythread extends  Thread {

    private int threadNumber;

    public FirstMultythread(int threadNumber){
        this.threadNumber = threadNumber;

    }
    @Override
    public void run(){
        for (int i = 0; i < 6; i++){
            System.out.println(i + " from thread -> " + this.threadNumber);
            // if (this.threadNumber == 2)
            //     throw new RuntimeException();
            
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
package design_patterns_java.Prototype;

/**
 * A prototype design pattern allow you to return a clone of a "prototype" object instead of initializing
 * an object using a constructor.
 * The constructor is private here as we can see.
 */

public class ConcreteCar {
    private String Model;
    private String Company;
    private  int year;

    private ConcreteCar(String model, String company, int year){
        this.Model=model;
        this.Company=company;
        this.year=year;
    }

    public static ConcreteCar getClone(){
        return new ConcreteCar("I10", "Mazda", 2030);
    }

    public String getModel() {
        return Model;
    }

    public void setModel(String model) {
        Model = model;
    }

    public String getCompany() {
        return Company;
    }

    public void setCompany(String company) {
        Company = company;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }


}

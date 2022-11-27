package Lesson5;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class CarArray {
    private ArrayList<Car> lot;

    public CarArray(ArrayList<Car> lot) {
        this.lot = lot;
    }

    public CarArray() {
        this.lot = new ArrayList<>();
    }

    public void toJson() throws IOException {
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.setPrettyPrinting().create();
        FileWriter fw = new FileWriter("carArray.json");
        String json = gson.toJson(this);
        fw.write(json);
        fw.close();
    }

    public static CarArray fromJson() throws IOException {
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.setPrettyPrinting().create();
        FileReader fr = new FileReader("carArray.json");
        CarArray ca = gson.fromJson(fr, CarArray.class);
        fr.close();
        return ca;
    }

    @Override
    public String toString() {
        return "CarArray{" +
                "lot=" + lot +
                '}';
    }

    public static void main(String[] args) throws IOException {
        Car c = new Car("Ford", "Ofri Tavor", 84, 2022);
        Car c1 = new Car("Ford", "Ofri Tavor1", 83, 2023);
        Car c2 = new Car("Ford", "Ofri Tavor2", 82, 2024);
        Car c3 = new Car("Ford", "Ofri Tavor3", 81, 9001);
        ArrayList<Car> lot = new ArrayList<>();
        lot.add(c);
        lot.add(c1);
        lot.add(c2);
        lot.add(c3);
        CarArray ca=new CarArray(lot);
        ca.toJson();
        CarArray ca2= CarArray.fromJson();
        System.out.println(ca2);
    }
}

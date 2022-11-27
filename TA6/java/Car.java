package Lesson5;

import com.google.gson.*;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Type;

public class Car {
    private String Company;
    private String Owner;
    private int id;
    private int Year;

    public static Car deserialize(String file) throws IOException {
        FileReader fr = new FileReader(file);
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.setPrettyPrinting().create();
        JsonDeserializer<Car> deserializer = new JsonDeserializer<Car>() {
            @Override
            public Car deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context) throws
                    JsonParseException {
                JsonObject jsonObject = json.getAsJsonObject();
                Car car = new Car(
                        jsonObject.get("Company").getAsString(),
                        jsonObject.get("Owner").getAsString(),
                        jsonObject.get("id").getAsInt(),
                        jsonObject.get("Year").getAsInt()
                );
                return car;
            }
        };
        builder.registerTypeAdapter(Car.class, deserializer);
        Gson g = builder.create();
        Car car = g.fromJson(fr, Car.class);
        fr.close();
        return car;
    }

    public void serialize(String file) throws IOException {
        GsonBuilder builder = new GsonBuilder().setPrettyPrinting();
        FileWriter fw = new FileWriter(file);
        Gson gson = builder.setPrettyPrinting().create();
//        JsonSerializer<Car> serializer = new JsonSerializer<Car>() {
//            @Override
//            public JsonElement serialize(Car car, Type type, JsonSerializationContext jsonSerializationContext) {
//                JsonObject obj = new JsonObject();
//                obj.addProperty("Company", car.Company);
//                obj.addProperty("Owner", car.Owner);
//                obj.addProperty("id", car.id);
//                obj.addProperty("Year", car.Year);
//                return obj;
//            }
//        };
        JsonObject obj = new JsonObject();
        obj.addProperty("Company", this.Company);
        obj.addProperty("Owner", this.Owner);
        obj.addProperty("id", this.id);
        obj.addProperty("Year", this.Year);
        gson.toJson(obj, fw);
        fw.close();
    }

    public Car(String company, String owner, int id, int year) {
        Company = company;
        Owner = owner;
        this.id = id;
        this.Year = year;
    }

    public void toJson() throws IOException {
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.setPrettyPrinting().create();
        FileWriter fw = new FileWriter("car.json");
        String json = gson.toJson(this);
        fw.write(json);
        fw.close();
        System.out.println(json);
    }


    public static Car fromJson() throws FileNotFoundException {
        GsonBuilder builder = new GsonBuilder();
        Gson gson = builder.create();
        FileReader fr = new FileReader("car.json");
        Car c = gson.fromJson(fr, Car.class);
        return c;
    }

    @Override
    public String toString() {
        return "Car{" +
                "Company='" + Company + '\'' +
                ", Owner='" + Owner + '\'' +
                ", id='" + id + '\'' +
                ", Year=" + Year +
                '}';
    }

    public static void main(String[] args) throws IOException {
        Car c = new Car("Ford", "Ofri Tavor", 8, 2022);
//        c.toJson();
//        Car c2 = Car.fromJson();
//        System.out.println(c2);
//        Car c3 = Car.deserialize("car.json");
//        System.out.println(c3);
        c.serialize("car.json");
    }
}


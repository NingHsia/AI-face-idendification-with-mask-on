#include <Adafruit_MLX90614.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  mlx.begin();

}

void loop()
{

  Serial.println(mlx.readObjectTempC());

  delay(1000);

}

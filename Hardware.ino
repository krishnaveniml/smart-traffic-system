int greenPins[4] = {23, 21, 18, 17};
int redPins[4]   = {22, 19, 5, 16};

int vehicleCount[4];
int greenTime[4] = {60, 45, 35, 30}; // seconds

String laneNames[4] = {"A","B","C","D"};

void setup() {
  Serial.begin(115200);

  for(int i=0;i<4;i++){
    pinMode(greenPins[i], OUTPUT);
    pinMode(redPins[i], OUTPUT);
  }
}

void loop() {

  if(Serial.available()){

    String data = Serial.readStringUntil('\n');

    int a,b,c,d;
    sscanf(data.c_str(), "%d,%d,%d,%d", &a,&b,&c,&d);

    vehicleCount[0]=a;
    vehicleCount[1]=b;
    vehicleCount[2]=c;
    vehicleCount[3]=d;

    runTraffic();
  }
}

void runTraffic(){

  int index[4]={0,1,2,3};

  // Sort highest to lowest
  for(int i=0;i<3;i++){
    for(int j=i+1;j<4;j++){
      if(vehicleCount[index[j]] > vehicleCount[index[i]]){
        int temp=index[i];
        index[i]=index[j];
        index[j]=temp;
      }
    }
  }

  for(int i=0;i<4;i++){

    int lane = index[i];

    // All red first
    for(int j=0;j<4;j++){
      digitalWrite(redPins[j],HIGH);
      digitalWrite(greenPins[j],LOW);
    }

    digitalWrite(redPins[lane],LOW);
    digitalWrite(greenPins[lane],HIGH);

    Serial.print("Lane ");
    Serial.print(laneNames[lane]);
    Serial.println(" GREEN");

    delay(greenTime[i] * 1000);
  }
}
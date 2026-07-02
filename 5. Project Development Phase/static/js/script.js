const sampleData = [
{
    nitrogen:90, phosphorus:42, potassium:43, temperature:20.87, humidity:82, ph:6.5, rainfall:202.93 // Rice
},
{
    nitrogen:77, phosphorus:58, potassium:30, temperature:25, humidity:60, ph:6.2, rainfall:85 // Maize
},
{
    nitrogen:40, phosphorus:67, potassium:79, temperature:20, humidity:18, ph:7.2, rainfall:80 // Chickpea
},
{
    nitrogen:100, phosphorus:75, potassium:50, temperature:27, humidity:80, ph:6.5, rainfall:105 // Banana
},
{
    nitrogen:20, phosphorus:27, potassium:30, temperature:30, humidity:50, ph:5.8, rainfall:95 // Mango
},
{
    nitrogen:24, phosphorus:132, potassium:198, temperature:24, humidity:81, ph:6.5, rainfall:70 // Grapes
},
{
    nitrogen:20, phosphorus:130, potassium:200, temperature:22, humidity:90, ph:6.2, rainfall:110 // Apple
},
{
    nitrogen:21, phosphorus:16, potassium:30, temperature:27, humidity:95, ph:5.5, rainfall:175 // Coconut
},
{
    nitrogen:120, phosphorus:40, potassium:20, temperature:25, humidity:80, ph:6.0, rainfall:95 // Cotton
},
{
    nitrogen:101, phosphorus:15, potassium:40, temperature:24, humidity:55, ph:6.0, rainfall:150 // Coffee
}
];

function fillSampleData() {

    const sample = sampleData[Math.floor(Math.random() * sampleData.length)];

    document.getElementsByName("nitrogen")[0].value = sample.nitrogen;
    document.getElementsByName("phosphorus")[0].value = sample.phosphorus;
    document.getElementsByName("potassium")[0].value = sample.potassium;
    document.getElementsByName("temperature")[0].value = sample.temperature;
    document.getElementsByName("humidity")[0].value = sample.humidity;
    document.getElementsByName("ph")[0].value = sample.ph;
    document.getElementsByName("rainfall")[0].value = sample.rainfall;
}

window.onload = function () {

    const result = document.getElementById("result");

    if(result){

        result.scrollIntoView({
            behavior:"smooth"
        });

    }

};
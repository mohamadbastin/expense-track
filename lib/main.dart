import 'dart:convert';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';


final prefs = SharedPreferences.getInstance();


void main() {
  runApp(MaterialApp(
    initialRoute: '/',
    routes: {
      '/': (context) => SplashScreen(),
      '/signup': (context) => Signup(),
      //   '/check': (context) => Check(),
    },
    title: 'Expense Track',
    // home: TutorialHome(),
    theme: ThemeData(primaryColor: Colors.white),
  ));
}

////////////////////// SPLASH SCREEN ///////////////////////

class SplashScreen extends StatefulWidget {
  @override
  _SplashState createState() => _SplashState();
}

class _SplashState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    Timer(Duration(seconds: 5), () => Navigator.pushNamed(context, '/signup'));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        fit: StackFit.expand,
        children: <Widget>[
          Container(
            decoration: BoxDecoration(color: Color(0xFF393e46)),
          ),
          Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: <Widget>[
              Expanded(
                flex: 2,
                child: Container(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Image.asset('images/logo.png'),
                      Padding(
                        padding: EdgeInsets.only(top: 10.0),
                      ),
                      Text(
                        'Expense Track',
                        style: TextStyle(
                            color: Color(0xFF4caf50),
                            fontWeight: FontWeight.bold,
                            letterSpacing: 5.0,
                            // backgroundColor: Colors.white,
                            fontSize: 30.0),
                      )
                    ],
                  ),
                ),
              ),
            ],
          )
        ],
      ),
    );
  }
}

//////////////////// SIGNUP PAGE /////////////////////

class Signup extends StatefulWidget {
  @override
  _SignupState createState() => _SignupState();
}

class _SignupState extends State<Signup> {
  final myController = TextEditingController();
  final mySecondController = TextEditingController();
  // Map data = {};

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: new GestureDetector(
      onTap: () {
        FocusScope.of(context).requestFocus(new FocusNode());
      },
      child: Stack(
        fit: StackFit.expand,
        children: <Widget>[
          Container(
            decoration: BoxDecoration(color: Color(0xFF393e46)),
          ),
          Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Expanded(
                child: Container(
                  child: Column(
                    children: <Widget>[
                      Padding(padding: EdgeInsets.all(90)),
                      Container(
                          width: 250,
                          child: TextField(
                            // focusNode: focusphone,
                            controller: myController,
                            textInputAction: TextInputAction.go,
                            style: TextStyle(color: Color(0xFF4caf50)),
                            keyboardType: TextInputType.text,
                            decoration: InputDecoration(
                              border: InputBorder.none,
                              icon: Icon(
                                Icons.account_circle,
                                color: Color(0xFF4caf50),
                                size: 50,
                              ),
                              labelText: 'Username',
                              labelStyle: TextStyle(color: Color(0xFF4caf50)),
                              // enabledBorder: UnderlineInputBorder(
                              //     borderSide: BorderSide(color: Colors.black, width: 0.0)),
                              // hintText: 'Enter Your Phone Number',
                              // prefix: Text('+98'),
                              hintStyle: TextStyle(color: Color(0xFF4caf50)),
                              fillColor: Color(0xFF4caf50),
                              // filled: true
                            ),
                          )),
                      Padding(padding: EdgeInsets.all(10)),
                      Container(
                          width: 250,
                          child: TextField(
                            // focusNode: focusphone,
                            controller: mySecondController,
                            obscureText : true,
                            textInputAction: TextInputAction.go,
                            style: TextStyle(color: Color(0xFF4caf50)),
                            keyboardType: TextInputType.text,
                            decoration: InputDecoration(
                              border: InputBorder.none,
                              icon: Icon(
                                Icons.vpn_key,
                                color: Color(0xFF4caf50),
                                size: 50,
                              ),
                              labelText: 'Password',
                              labelStyle: TextStyle(color: Color(0xFF4caf50)),
                              // enabledBorder: UnderlineInputBorder(
                              //     borderSide: BorderSide(color: Colors.black, width: 0.0)),
                              // hintText: 'Enter Your Phone Number',
                              // prefix: Text('+98'),
                              hintStyle: TextStyle(color: Color(0xFF4caf50)),
                              fillColor: Color(0xFF4caf50),
                              // filled: true
                            ),
                          )),
                      Padding(
                        padding: EdgeInsets.all(15),
                      ),
                      RaisedButton(
                        color: Color(0xFF4caf50),
                        child: Text('sign up'),
                        onPressed: () {

                          if (myController.text != null &&
                              mySecondController.text!=null) {
                            
                            Map data = {'username': myController.text, 'password': mySecondController.text};

                            showDialog(
                                
                                context: context,
                                builder: (context) {
                                  return AlertDialog(
                                    contentPadding: EdgeInsets.all(0.0),
                                    titlePadding: EdgeInsets.all(0.0),
                                    content: Container(
                                      child: Image.asset('images/loader.gif'),
                                      height: 100,
                                      width: 100,
                                    )
                                  );
                                });
                            Future <http.Response> signin() async {
                            http.post(
                                  'http://127.0.0.1:8000/api-token-auth/',
                                  body: json.encode(data),
                                  headers: {
                                    "Accept": "application/json",
                                    "content-type": "application/json"
                                  }).then((http.Response response) {
                                    var a =  (json.decode(response.body)["token"]);
                                    prefs.setInt('token', 1);
                                    print(prefs.getInt('token'));
                                    // Navigator.pop(context);
                                    // Navigator.pushNamed(
                                    //   context,
                                    //   '/check',
                                    // );
                                  });

              

              // return showDialog(
              //     context: context,
              //     builder: (context) {
              //       return AlertDialog(
              //         content: Text('done'),
              //       );
              //     });
              
            }

            signin();
          } else {}

                            },
                        ),
                    ],
                  ),
                ),
              )
            ],
          )
        ],
      ),
    ));
  }
}

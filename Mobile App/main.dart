import 'package:flutter/material.dart';
import 'dart:io';
import 'dart:ui';
import 'package:path_provider/path_provider.dart';
// Amplify Flutter Packages
import 'package:amplify_flutter/amplify_flutter.dart';

import 'package:amplify_storage_s3/amplify_storage_s3.dart';

import 'package:amplify_flutter/amplify_flutter.dart';
import 'package:amplify_auth_cognito/amplify_auth_cognito.dart';
import 'package:amplify_storage_s3/amplify_storage_s3.dart';
import 'package:ledy/amplifyconfiguration.dart';
import 'package:amplify_api_plugin_interface/amplify_api_plugin_interface.dart';

Future<void> createAndUploadFile() async {
  // Create a dummy file
  final exampleString = 'Example file contents';
  final tempDir = await getTemporaryDirectory();
  final exampleFile = File(tempDir.path + '/mode.txt')
    ..createSync()
    ..writeAsStringSync(exampleString);

  print("plik stworzony i zapisany");
  // Upload the file to S3
  //AmplifyAPI apiPlugin = AmplifyAPI();
  AmplifyStorageS3 storagePlugin = AmplifyStorageS3();

  //await Amplify.addPlugins([AmplifyAuthCognito(), AmplifyStorageS3(), storagePlugin]);
  print("zaraza");
  try {
    await Amplify.configure(amplifyconfig);
  } on AmplifyAlreadyConfiguredException {
    print("juz skonfigurowane");
  }
  print("part2");
  try {
    print("próba uploadu");

    final UploadFileResult result = await Amplify.Storage.uploadFile(
        local: exampleFile,
        key: 'mode.txt',
        onProgress: (progress) {
          print("Fraction completed: " +
              progress.getFractionCompleted().toString());
        }
    );
    print("po probie");
    print('Successfully uploaded file: ${result.key}');
  } on StorageException catch (e) {
    print('Error uploading file: $e');
  }

  print("po wszystkim");
}


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);



  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Ledy w moim pokoju',
        home: Scaffold(
          appBar: AppBar(title: const Text('Ledy w moim pokoju', style: const TextStyle(color: Colors.black87),),
            backgroundColor: Colors.yellow,),
          backgroundColor: Colors.white12,
          body: Center(
            child: OutlinedButton(onPressed: () => createAndUploadFile(), child: Text("zmien", style: TextStyle(color: Colors.black87),),
              style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.yellow)),),
          ),
        )
    );
  }
}

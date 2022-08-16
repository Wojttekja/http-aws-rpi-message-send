# Light-control-app
eng:
Javascript React website as remote controller --> sends http request to AWS ApiGateway --> triggers AWS Lambda --> AWS Lambda turns body of http request to .txt file and sends it to AWS S3 bucket --> every some amount of time (probably ~15 seconds) Python script running on Raspberry Pi checks if .txt file has changed --> if changed downloads it and changes mode

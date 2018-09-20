# Multimodal Prediction of Audience's Impression in Political Debates

Source code and data (raw and preprocessed) for training multimodal approaches to predict the impression given by politicians in TV debates.

https://www.ukp.tu-darmstadt.de

https://www.tu-darmstadt.de

Project maintainer: Pedro Santos (@pedrobisp)

This repository contains experimental software and is published for the sole purpose of giving additional background details.

The transcripts and impression scores are available by request.
Please contact the project maintainer for obtaining these resources: https://www.informatik.tu-darmstadt.de/ukp/ukp_home/staff_ukp/detailseite_mitarbeiter_1_42304.en.jsp

Due to legal issues, we cannot redistribute the debate recording.
However, the debate is publicly available online at YouTube: https://youtu.be/Hybsgj1MIZ4

We used Python 3 in our experiments, so we recommend also using it to reproduce the experiments.
We also recommend using a virtual enviroment.
The packages used in our experiments can be installed by the following command

```
pip3 install -r requirements.txt
```

Besides that, we also used third party open source software for preprocessing the debate video file:

* FFmpeg - https://www.ffmpeg.org/

* OpenFace - https://github.com/TadasBaltrusaitis/OpenFace

The debate is segmented into turns, where each turn consists of a politician talking without a major interruption by the other politician or one of the journalists.
Small interruptions can occur though.
So, the first step for preprocessing the debate video file is to segment it in turns.


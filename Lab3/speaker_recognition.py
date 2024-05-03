import numpy as np
import librosa
from tensorflow.keras import layers, models, utils
import tensorflow as tf
from tensorflow import keras




# Function to extract MFCC features from audio files
def extract_features(file_path, mfcc=True, chroma=True, mel=True,sr=22050):
    audio_data, _ = librosa.load(file_path)  # Load audio data directly without a context manager
    features = []
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13), axis=1)
        features.extend(mfccs)
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(y=audio_data, sr=sr), axis=1)
        features.extend(chroma)
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(y=audio_data, sr=sr), axis=1)
        features.extend(mel)
    return features



if __name__ == '__main__':

    sr=22050
    class_names = ["cyhh","haoyu","stranger"]
    # Load the model
    model = tf.keras.models.load_model('speaker_recognition_model')
    # preprocessing
    test_feature= extract_features("test_audio/test.wav", mfcc=True, chroma=True, mel=True,sr=22050)
    # test_feature= extract_features("audio_files/haoyu_audio_70.wav", mfcc=True, chroma=True, mel=True,sr=22050)
    print(len(test_feature))
    test_feature= np.array(test_feature)
    # print(test_feature.shape)
    test_feature= test_feature.reshape(1,153,1)
    # print(test_feature.shape)

    # Make prediction

    predictions = model.predict(test_feature)
    print(predictions)
    # Post-process predictions (e.g., choose the class with the highest probability)
    predicted_label = np.argmax(predictions)

    print("Predicted label:", class_names[predicted_label])
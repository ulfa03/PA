from tensorflow.keras.models import load_model

model = load_model("model_vgg16.h5z23_gfva.h5", compile=False)
model.summary()

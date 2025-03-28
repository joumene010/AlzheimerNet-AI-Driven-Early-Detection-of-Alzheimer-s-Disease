# **AlzheimerNet: AI-Driven Early Detection of Alzheimer’s Disease**  

![Streamlit Interface Demo](assets/streamlit_demo.png)  

## **📌 Overview**  
AlzheimerNet is a deep learning-based system designed to classify brain MRI scans for early detection of **Alzheimer’s Disease (AD)**. The project includes **two versions**:  
- **Version 1 (4-class classification):** Detects **Non-Demented, Very Mild Demented, Mild Demented, and Moderate Demented** cases.  
- **Version 2 (3-class classification):** Classifies **Cognitively Normal (CN), Mild Cognitive Impairment (MCI), and Alzheimer’s Disease (AD)**.  

Both versions leverage **Convolutional Neural Networks (CNNs)** and **transfer learning** to improve diagnostic accuracy.  

---

## **🚀 Key Features**  
### **Version 1 (4-Class Classification)**  
✅ **Classes:** Non-Demented, Very Mild Demented, Mild Demented, Moderate Demented  
✅ **Custom CNN Model:** Achieved **86% accuracy**  
✅ **Challenges:** Struggled with **Moderate Demented** class due to data imbalance  

### **Version 2 (3-Class Classification)**  
✅ **Classes:** Cognitively Normal (CN), Mild Cognitive Impairment (MCI), Alzheimer’s Disease (AD)  
✅ **Improved Accuracy:** **98%** on test set  
✅ **Simplified Task:** Better performance due to reduced complexity  

### **Shared Features**  
🔹 **Data Augmentation:** Rotation, flipping, zooming, shearing  
🔹 **Pretrained Models Tested:** ResNet, EfficientNet, MobileNet (**ResNet performed best at 64.21%**)  
🔹 **Streamlit Web App:** User-friendly interface for MRI upload and prediction  

---

## **🛠️ Installation & Setup**  
### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/AlzheimerNet.git  
cd AlzheimerNet  
```

### **2. Install Dependencies**  
```bash
pip install -r requirements.txt  
```

### **3. Run the Streamlit App (for predictions)**  
```bash
streamlit run src/app.py  
```

---

## **📂 Repository Structure**  
```
AlzheimerNet/  
├── version_1/                # 4-Class Classification  
│   ├── data/                 # Preprocessed MRI dataset  
│   ├── models/               # Saved model weights (custom CNN)  
│   ├── notebooks/            # Training & evaluation notebooks  
│   └── src/                  # Preprocessing & training scripts  
│  
├── version_2/                # 3-Class Classification  
│   ├── data/                 # Preprocessed MRI dataset  
│   ├── models/               # Saved model weights  
│   ├── notebooks/            # Training & evaluation notebooks  
│   └── src/                  # Preprocessing & training scripts  
│  
├── assets/                   # Demo images, graphs  
├── reports/                  # Project report (PDF)  
└── README.md  
```

---

## **📊 Results Summary**  
| **Metric**       | **Version 1 (4-Class)** | **Version 2 (3-Class)** |  
|------------------|----------------------|----------------------|  
| **Accuracy**     | 86%                 | 98%                 |  
| **Best Model**   | Custom CNN          | Custom CNN          |  
| **Pretrained Best** | ResNet (64.21%)  | ResNet (64.21%)*    |  

_*Pretrained models were tested on Version 1 but can be adapted for Version 2._  

---

## **🔮 Future Improvements**  
- **Expand dataset** with PET scans and longitudinal studies  
- **Test Vision Transformers (ViT)** for better feature extraction  
- **Improve explainability** using Grad-CAM/SHAP  
- **Federated learning** for privacy-preserving multi-hospital collaboration  


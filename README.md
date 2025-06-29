# Adaptive Hierarchical Vector Database

## Overview

This project presents an advanced **vector database system** built from scratch, designed to improve the efficiency and accuracy of similarity-based retrieval in high-dimensional data. It introduces an **adaptive hierarchical clustering algorithm** that reduces query time, enhances semantic representation, and enables support for **multi-cluster membership**.

By integrating dynamic restructuring, weighted centroid updates, and a two-pass skip algorithm, this approach significantly outperforms traditional flat-index and single-layer centroid models — achieving up to **36× faster retrieval** on real-world text, image, and statistical datasets.

---

## Key Features

- ⚡ **Fast Vector Retrieval**: Multi-level clustering significantly reduces the number of comparisons required during query.
- 🔄 **Adaptive Tree Construction**: Customizable tree depth and dynamic restructuring enable scalability for growing datasets.
- 🧠 **Context-Preserving Centroids**: Weighted centroid updates retain semantic meaning during clustering.
- 🔀 **Multi-Cluster Membership**: Skip algorithm avoids premature classification and accurately assigns vectors to multiple clusters.
- 🧪 **Cross-Domain Evaluation**: Validated on NLP (text embeddings), computer vision (image embeddings), and statistical (tabular) datasets.

---

## Architecture

![flowchart](https://github.com/user-attachments/assets/86de8ec9-ceba-4690-a23a-b2e6da925fa2)

---

## Technologies Used

- **Languages**: Python
- **Libraries**: 
  - `PyTorch`, `TensorFlow`, `scikit-learn`
  - `Hugging Face Transformers` (for BERT/RoBERTa)
  - `OpenCV`, `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`
- **Tools**: Jupyter Notebook, Docker

---

## Datasets

- 📝 **Text**: Research articles embedded with BERT/RoBERTa.
- 🖼️ **Images**: Plant Disease dataset from Kaggle with ResNet/EfficientNet embeddings.
- 📊 **Statistical**: PUBG player stats dataset with pre-existing numerical features.

---

## Performance

| Dataset      | Avg Query Time (Baseline) | Avg Query Time (Ours) | Speedup |
|--------------|---------------------------|------------------------|---------|
| Text         | 1.45s                     | 0.04s                  | 36×     |
| Images       | 2.10s                     | 0.14s                  | 15×     |
| Statistics   | 0.038s                    | 0.002s                 | 19×     |

F1-scores remained stable or improved in all domains, showcasing the model’s robustness.

---

## Limitations

- ❌ Requires separate trees for different modalities (text/image/stats).
- 🕒 High construction time (~2–4 hours per domain).
- 📦 Increased memory consumption due to hierarchical structure.
- 🔁 Currently static — incremental updates not yet supported.

---

## Future Work

- Support for **cross-modal embeddings**
- Enable **incremental updates** for dynamic data
- Explore **parallelized tree construction**
- Integrate **non-linear transformations** for dimension adjustment

---

## Authors

- Kathan Piyushkumar Bhavsar  
- Kalp Jigneshbhai Kalani  
- Dev Pinakinbhai Patel  
- Kush Janak Patel  
- Mohammad Arsh Vahora  
- Hetanshu Hemant Patel  

University of Windsor, 2025

---

## License

This project is developed for academic and research purposes. For any commercial or production usage, please contact the authors.

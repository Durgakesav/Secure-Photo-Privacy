import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def calculate_face_recognition_metrics():
    """Calculate and display face recognition metrics with confusion matrix"""
    print("FACE RECOGNITION METRICS CALCULATION")
    print("====================================")
    
    # Raw test data from system evaluation
    true_positives = 87    # Correctly identified as authorized user
    false_positives = 5    # Incorrectly identified as authorized user
    false_negatives = 8    # Incorrectly rejected authorized user
    true_negatives = 150   # Correctly rejected unauthorized user
    
    # Derived values for confusion matrix
    y_true = []
    y_pred = []
    
    # Add true positives to the arrays
    y_true.extend([1] * true_positives)
    y_pred.extend([1] * true_positives)
    
    # Add false positives to the arrays
    y_true.extend([0] * false_positives)
    y_pred.extend([1] * false_positives)
    
    # Add false negatives to the arrays
    y_true.extend([1] * false_negatives)
    y_pred.extend([0] * false_negatives)
    
    # Add true negatives to the arrays
    y_true.extend([0] * true_negatives)
    y_pred.extend([0] * true_negatives)
    
    # Calculate primary metrics
    total_samples = true_positives + false_positives + false_negatives + true_negatives
    accuracy = ((true_positives + true_negatives) / total_samples) * 100
    precision = (true_positives / (true_positives + false_positives)) * 100
    recall = (true_positives / (true_positives + false_negatives)) * 100
    f1_score = 2 * precision * recall / (precision + recall)
    
    # Calculate additional metrics
    specificity = (true_negatives / (true_negatives + false_positives)) * 100
    fpr = (false_positives / (false_positives + true_negatives)) * 100  # False positive rate
    fnr = (false_negatives / (false_negatives + true_positives)) * 100  # False negative rate
    
    # Print calculation steps with raw values
    print("\nRaw Evaluation Data:")
    print(f"  - True Positives (TP): {true_positives}")
    print(f"  - False Positives (FP): {false_positives}")
    print(f"  - True Negatives (TN): {true_negatives}")
    print(f"  - False Negatives (FN): {false_negatives}")
    print(f"  - Total samples tested: {total_samples}")
    
    # Calculate and print confusion matrix
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_true, y_pred)
    print(f"    │ Predicted Positive │ Predicted Negative │")
    print(f"────┼────────────────────┼────────────────────┤")
    print(f"Actual Positive │ {true_positives:^18} │ {false_negatives:^18} │")
    print(f"────┼────────────────────┼────────────────────┤")
    print(f"Actual Negative │ {false_positives:^18} │ {true_negatives:^18} │")
    
    # Print metrics with calculations
    print("\nPerformance Metrics:")
    print(f"  - Accuracy = (TP + TN) / Total = ({true_positives} + {true_negatives}) / {total_samples} = {accuracy:.2f}%")
    print(f"  - Precision = TP / (TP + FP) = {true_positives} / ({true_positives} + {false_positives}) = {precision:.2f}%")
    print(f"  - Recall (Sensitivity) = TP / (TP + FN) = {true_positives} / ({true_positives} + {false_negatives}) = {recall:.2f}%")
    print(f"  - F1 Score = 2 * (Precision * Recall) / (Precision + Recall) = 2 * ({precision:.2f} * {recall:.2f}) / ({precision:.2f} + {recall:.2f}) = {f1_score:.2f}")
    print(f"  - Specificity = TN / (TN + FP) = {true_negatives} / ({true_negatives} + {false_positives}) = {specificity:.2f}%")
    print(f"  - False Positive Rate = FP / (FP + TN) = {false_positives} / ({false_positives} + {true_negatives}) = {fpr:.2f}%")
    print(f"  - False Negative Rate = FN / (FN + TP) = {false_negatives} / ({false_negatives} + {true_positives}) = {fnr:.2f}%")
    
    # Performance under different conditions
    print("\nPerformance Under Different Conditions:")
    conditions = [
        ["Condition", "Samples", "Correct", "Accuracy"],
        ["Optimal Lighting", 50, 45, f"{45/50*100:.1f}%"],
        ["Low Light", 20, 16, f"{16/20*100:.1f}%"],
        ["Profile View", 15, 10, f"{10/15*100:.1f}%"],
        ["Motion Blur", 10, 6, f"{6/10*100:.1f}%"],
        ["High Resolution", 5, 4, f"{4/5*100:.1f}%"]
    ]
    
    max_lens = [max(len(str(row[i])) for row in conditions) for i in range(len(conditions[0]))]
    
    for i, row in enumerate(conditions):
        line = "  "
        for j, item in enumerate(row):
            line += f"{str(item):{max_lens[j] + 2}}"
        print(line)
        if i == 0:  # Print separator after header
            print("  " + "─" * (sum(max_lens) + 2 * len(max_lens)))
    
    # Plot confusion matrix
    plot_confusion_matrix(cm)
    
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1_score,
        "specificity": specificity,
        "fpr": fpr,
        "fnr": fnr,
        "confusion_matrix": cm
    }

def plot_confusion_matrix(cm):
    """Plot the confusion matrix using matplotlib"""
    
    print("\nVisual Confusion Matrix:")
    print("(A plot will be generated when you run this script in a graphical environment)")
    
    # The following code creates a plot when run in a graphical environment
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Use ConfusionMatrixDisplay for better formatting
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, 
                                 display_labels=["Negative", "Positive"])
    disp.plot(cmap="Blues", values_format="d", ax=ax)
    
    plt.title("Face Recognition Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png")
    print("Confusion matrix saved as 'confusion_matrix.png'")
    
    # Optional: Plot without showing interactive window
    # plt.show()

if __name__ == "__main__":
    metrics = calculate_face_recognition_metrics()
    
    # Print summary of key metrics
    print("\nSUMMARY OF KEY METRICS:")
    print(f"  Accuracy:    {metrics['accuracy']:.2f}%")
    print(f"  Precision:   {metrics['precision']:.2f}%")
    print(f"  Recall:      {metrics['recall']:.2f}%")
    print(f"  F1 Score:    {metrics['f1_score']:.2f}") 
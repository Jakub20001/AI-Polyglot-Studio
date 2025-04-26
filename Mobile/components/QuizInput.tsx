import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

interface QuizInputProps {
    question: string,
    onSubmit: (answer: string) => void;
}

const QuizInput: React.FC<QuizInputProps> = ({ question, onSubmit }) => {
    const [answer, setAnswer] = useState('');

    const handleSubmit = () => {
        if (!answer.trim()) return;
        onSubmit(answer.trim());
        setAnswer('');
    };

    return (
        <View style={styles.container}>
            <Text style={styles.question}>{question}</Text>
            <TextInput
              style={styles.input}
              placeholder="Enter your answer..."
              value={answer}
              onChangeText={setAnswer}            
            />
            <TouchableOpacity style={styles.button} onPress={handleSubmit}>
                <Text style={styles.buttonText}>Submit Answer</Text>
            </TouchableOpacity>
        </View>
    );
};

export default QuizInput;

const styles = StyleSheet.create({
    container: {
        marginVertical: 20,
        paddingHorizontal: 20,
    },
    question: {
        fontSize: 18,
        fontWeight: '700',
        marginBottom: 12,
        color: '#1f2937',
        textAlign: 'center',
    },
    input: {
        borderColor: '#d1d5db',
        borderWidth: 1,
        borderRadius: 8,
        paddingHorizontal: 12,
        paddingVertical: 8,
        fontSize: 16,
        marginBottom: 12,
    },
    button: {
        backgroundColor: '#10b981',
        paddingVertical: 12,
        borderRadius: 8,
        alignItems: 'center',
    },
    buttonText: {
        color: '#ffffff',
        fontWeight: '600',
        fontSize: 16,
    },
});
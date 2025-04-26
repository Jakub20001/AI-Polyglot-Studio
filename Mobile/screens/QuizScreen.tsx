import React from 'react';
import { View, Text, StyleSheet, ScrollView, } from 'react-native';
import QuizInput from '../components/QuizInput';

const QuizScreen: React.FC = () => {
    const handleAnswerSubmit = (answer: string) => {
        console.log("User answer:", answer);
    };

    return (
        <ScrollView contentContainerStyle={styles.container}>
            <Text style={styles.title}>Language Quiz</Text>
            <QuizInput question="Translate 'Good morning' into Spanish." onSubmit={handleAnswerSubmit} />
        </ScrollView>
    );
};

export default Screen;

const styles = StyleSheet.create({
    container: {
        padding: 20,
        flexGrow: 1,
        backgroundColor: '#f9fafb',
    },
    title: {
        fontSize: 24,
        fontWeight: '700',
        color: '#22c55e',
        marginBottom: 20,
    },
});
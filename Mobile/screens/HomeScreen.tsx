import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

const HomeScreen: React.FC = () => {
    return (
        <ScrollView contentContainerStyle={styles.container}>
            <Text style={styles.title}>Welcome to AI Polyglot Studio!</Text>
            <Text style={styles.subtitle}>
                Master languages with AI dialogues, quizzes, and your personal language mentor.
            </Text>
        </ScrollView>
    );
};

export default HomeScreen;

const styles = StyleSheet.create({
    container: {
        padding: 20,
        flexGrow: 1,
        justifyContent: 'center',
        backgroundColor: '#f9fafb',
    },
    title: {
        fontSize: 28,
        fontWeight: '700',
        color: '#2563eb',
        textAlign: 'center',
        marginBottom: 12,
    },
    subtitle: {
        fontSize: 16,
        color: '#6b7280',
        textAlign: 'center',
    },
});

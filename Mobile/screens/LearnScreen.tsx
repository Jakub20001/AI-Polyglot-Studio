import React from 'react';
import { View, Text, StyleSheet, ScrollView } from 'react-native';

const LearnScreen: React.FC = () => {
    return (
        <ScrollView contentContainerStyle={styles.container}>
            <Text style={styles.title}>Learning Modules</Text>
            <Text style={styles.text}>
                Select your target language, difficulty level, and topic to start interactive lessons powered by AI.
            </Text>
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
        color: '#2563eb',
        marginBottom: 16,
    },
    text: {
        fontSize: 16,
        color: '#4b5563',
        textAlign: 'left'
    },
});
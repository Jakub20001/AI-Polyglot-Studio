import React from 'react';
import { ScrollView, StyleSheet, Text } from 'react-native';
import MentorChat from '../components/MentorChat';

const MentorScreen: React.FC = () => {
    const mockAsk = async (question: string) => {
        console.log('User asked:', question);
        return `AI Mentor Response to: "${question}"`;
    };

    return (
        <ScrollView contentContainerStyle={styles.container}>
            <Text style={styles.title}>Ask Your AI Mentor</Text>
            <MentorChat onAsk={mockAsk}/>
        </ScrollView>
    );
};

export default MentorScreen

const styles = StyleSheet.create({
    container: {
        padding: 20,
        flexGrow: 1,
        backgroundColor: '#f9fafb',
    },
    title: {
        fontSize: 24,
        fontWeight: '700',
        color: '#ec4899',
        marginBottom: 16,
    },
});
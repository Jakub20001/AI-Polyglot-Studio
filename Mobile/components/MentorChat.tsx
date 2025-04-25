import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, StyleSheet, ActivityIndicator } from 'react-native';

interface MentorChatProps {
    onAsk: (question: string) => Promise<string>;
}

const MentorChat: React.FC<MentorChatProps> = ({ onAsk }) => {
    const [input, setInput] = useState('');
    const [response, setResponse] = useState('');
    const [loading, setLoading] = useState(false);

    const handleAsk = async () => {
        if (!input.trim()) return;
        setLoading(true);
        const res = await onAsk(input.trim());
        setResponse(res);
        setInput('');
        setLoading(false);
    };

    return (
        <View style={styles.container}>
            <Text style={styles.label}>Ask your Mentor</Text>
            <TextInput
              style={styles.input}
              placeholder="Type your question..."
              value={input}
              onChangeText={setInput}
            />
            <TouchableOpacity style={styles.button} onPress={handleAsk} disabled={loading}>
                <Text style={styles.buttonText}>{loading ? 'Asking...': 'Ask'}</Text>
            </TouchableOpacity>
        </View>
    );
};

export default MentorChat

const styles = StyleSheet.create({
    container: {
        marginTop: 20,
        paddingHorizontal: 20,
        flex: 1,
    },
    label: {
        fontSize: 18,
        fontWeight: '700',
        marginBottom: 8,
        color: '#374151',
    },
    input: {
        borderColor: '#d1d5db',
        borderWidth: 1,
        borderRadius: 8,
        paddingHorizontal: 12,
        paddingVertical: 8,
        marginBottom: 10,
        fontSize: 16,
    },
    button: {
        backgroundColor: '#2563eb',
        paddingVertical: 12,
        borderRadius: 8,
        alignItems: 'center',
    },
    buttonText: {
        color: '#fff',
        fontWeight: '600',
        fontSize: 16,
    },
    responseBox: {
        marginTop: 20,
        padding: 12,
        backgroundColor: '#f9fafb',
        borderRadius: 8,
        borderColor: '#e5e7eb',
        borderWidth: 1,
    },
    responseText: {
        fontSize: 16,
        color: '#111827',
    },



});


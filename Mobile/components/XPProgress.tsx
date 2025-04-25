import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface XPProgressProps {
    points: number;
    maxPoints?: number;
}

const XPProgress: React.FC<XPProgressProps> = ({ points, maxPoints = 100 }) => {
    const percentage = Math.min((points / maxPoints) * 100, 100);

    return (
        <View style={styles.container}>
            <Text style={styles.label}>XP Progress: {points} / {maxPoints}</Text>
            <View style={styles.progressBackground}>
                <View style={[styles.progressBar, { width:  `${percentage}%` }]} />
            </View>
        </View>
    );
};

export default XPProgress

const styles = StyleSheet.create({
    container: {
        marginVertical: 20,
        width: '90%',
        alignSelf: 'center',
    },
    label: {
        marginBottom: 8,
        fontSize: 16,
        fontWeight: '600',
        color: '#374151',
        textAlign: 'center',
    },
    progressBackground: {
        height: 16,
        backgroundColor: '#E5E7EB',
        borderRadius: 8,
        overflow: 'hidden',
    },
    progressBar: {
        height: 16,
        backgroundColor: '#22C55E',

    },
});

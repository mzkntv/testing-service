import { createRouter, createWebHistory } from 'vue-router'
import TestCasePage from "./components/TestCasePage.vue";
import TestCaseList from "./components/TestCaseList.vue";

const routes = [
    {
        path: '/',
        redirect: () => ({name: 'test-case-list'}),
    },
    {
        path: '/test-cases',
        component: TestCasePage,
        children: [
            {
                path: '',
                name: 'test-case-list',
                component: TestCaseList,
            },
            {
                path: ':testCaseId/processing',
                name: 'test-case-detail',
                props: route => ({testCaseId: route.params.testCaseId}),
                component: () => import('./components/TestCaseDetail.vue'),
            },
            {
                path: ':testCaseId/processing/:processingId/questions/:questionId',
                name: 'question-detail',
                props: route => ({
                    testCaseId: route.params.testCaseId,
                    processingId: route.params.processingId,
                    questionId: route.params.questionId,
                }),
                component: () => import('./components/QuestionCard.vue')
            },
            {
                path: ':testCaseId/processing/:processingId/results',
                name: 'test-case-results',
                props: route => ({
                    testCaseId: route.params.testCaseId,
                    processingId: route.params.processingId,
                }),
                component: () => import('./components/TestCaseResult.vue')
            },
        ]
    }
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
})

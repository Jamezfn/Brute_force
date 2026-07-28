export default {
	transform: {
		'^.+\\.tsx?$': ['@swc/jest'],
	},
	moduleNameMapper: {
		'^(\\.{1,2}/.*)\\.js$': '$1',
	},
	testEnvironment: 'node',
};
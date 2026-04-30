/**
 * Aviz Academy - GitHub Actions Test Script
 * Author: Avinash Reddy Thipparthi
 * Role: Cloud & DevOps Architect
 * 
 * Purpose:
 * Simple Node.js script to validate CI workflow execution.
 */

const os = require("os");

// Branding Banner
console.log("=====================================");
console.log("🚀 Aviz Academy - CI/CD Test Run");
console.log("👨‍💻 Avinash Reddy Thipparthi");
console.log("☁️  AWS | DevOps | Docker Captain");
console.log("📺 YouTube: @avizway");
console.log("=====================================\n");

// Basic Execution Check
console.log("✅ Script execution started...");

// Environment Info (useful for CI debugging)
console.log("\n🔍 Environment Details:");
console.log(`Platform   : ${os.platform()}`);
console.log(`Architecture: ${os.arch()}`);
console.log(`Node Version: ${process.version}`);

// Simulate Step
console.log("\n⚙️ Running sample validation...");
const result = 2 + 2;

if (result === 4) {
    console.log("✅ Validation successful: 2 + 2 = 4");
} else {
    console.error("❌ Validation failed");
    process.exit(1);
}

// GitHub Actions specific context check
if (process.env.GITHUB_ACTIONS) {
    console.log("\n🔗 Running inside GitHub Actions");
    console.log(`Workflow: ${process.env.GITHUB_WORKFLOW}`);
    console.log(`Repository: ${process.env.GITHUB_REPOSITORY}`);
} else {
    console.log("\nℹ️ Running locally");
}

// Final Output
console.log("\n🎯 CI Test Completed Successfully!");
console.log("=====================================");
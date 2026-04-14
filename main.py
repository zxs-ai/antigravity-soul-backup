import os
import tarfile
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
import threading

# Configuration
SOURCE_DIR = os.path.expanduser("~/.gemini/antigravity")
BACKUP_TARGETS = ["knowledge", "brain", "global_memory.yaml"]
DOWNLOADS_DIR = os.path.expanduser("~/Downloads")

BG_COLOR = "#FAF9F6"
TEXT_COLOR = "#2C2C2C"
BTN_BG = "#EAE7E0"
BTN_ACTIVE = "#D9D5CB"
ACCENT_COLOR = "#D97757"

class AntigravitySoulManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Antigravity Soul Manager")
        self.root.geometry("520x400")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)

        # Style Configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background=BG_COLOR)
        style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR, font=("Georgia", 13))
        style.configure("Header.TLabel", background=BG_COLOR, foreground=TEXT_COLOR, font=("Georgia", 22, "bold"))
        style.configure("Sub.TLabel", background=BG_COLOR, foreground="#666666", font=("Arial", 11))
        style.configure("Tip.TLabel", background=BG_COLOR, foreground="#888888", font=("Arial", 10))

        # Main Layout
        self.main_frame = ttk.Frame(self.root, padding="40")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Header Region
        self.header = ttk.Label(self.main_frame, text="Antigravity 灵魂容器", style="Header.TLabel")
        self.header.pack(pady=(0, 5))

        self.desc = ttk.Label(self.main_frame, text="备份或恢复你的 AI 记忆、规则约束及上下文约定", justify="center")
        self.desc.pack(pady=(0, 25))

        # Action Buttons
        self.btn_frame = ttk.Frame(self.main_frame)
        self.btn_frame.pack(pady=10)

        # Custom Buttons using Canvas for rounded effect (simple fallback to tk.Button for purity)
        self.backup_btn = tk.Button(self.btn_frame, text="✦ 导出完整灵魂", command=self.start_backup, 
                                   bg=ACCENT_COLOR, fg="white", font=("Arial", 13, "bold"), 
                                   padx=20, pady=10, borderwidth=0, cursor="hand2")
        self.backup_btn.pack(side=tk.LEFT, padx=15)

        self.restore_btn = tk.Button(self.btn_frame, text="⟲ 导入记忆备份", command=self.start_restore, 
                                    bg=BTN_BG, fg=TEXT_COLOR, font=("Arial", 13, "normal"), 
                                    padx=20, pady=10, borderwidth=0, cursor="hand2")
        self.restore_btn.pack(side=tk.LEFT, padx=15)

        # Tips
        self.path_tip = ttk.Label(self.main_frame, text="默认导出路径将在：你的系统「下载(Downloads)」文件夹", style="Tip.TLabel")
        self.path_tip.pack(pady=(25, 5))

        # Status Label
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(self.main_frame, textvariable=self.status_var, font=("Arial", 11), foreground=ACCENT_COLOR)
        self.status_label.pack(side=tk.BOTTOM, pady=(15, 0))

    def update_status(self, msg, color=ACCENT_COLOR):
        self.status_label.configure(foreground=color)
        self.status_var.set(msg)
        self.root.update_idletasks()

    def start_backup(self):
        self.update_status("正在备份，请等待 1-5 分钟。成功后会弹窗，请勿关闭本窗口...")
        self.backup_btn.config(state=tk.DISABLED)
        self.restore_btn.config(state=tk.DISABLED)
        threading.Thread(target=self.run_backup).start()

    def run_backup(self):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            filename = f"Antigravity_Soul_Backup_{timestamp}.tar.gz"
            dest_path = os.path.join(DOWNLOADS_DIR, filename)

            # Ensure source exists, dummy handle if missing
            if not os.path.exists(SOURCE_DIR):
                os.makedirs(SOURCE_DIR, exist_ok=True)

            with tarfile.open(dest_path, "w:gz") as tar:
                for target in BACKUP_TARGETS:
                    full_path = os.path.join(SOURCE_DIR, target)
                    if os.path.exists(full_path):
                        tar.add(full_path, arcname=target)
            
            self.update_status(f"✓ 成功导出至下载文件夹", color="#4CAF50")
            messagebox.showinfo("备份成功", f"记忆已封印！\n文件保存在: {dest_path}")
        except Exception as e:
            self.update_status("✗ 备份失败", color="#F44336")
            messagebox.showerror("错误", f"备份过程中出错: {str(e)}")
        finally:
            self.backup_btn.config(state=tk.NORMAL)
            self.restore_btn.config(state=tk.NORMAL)

    def start_restore(self):
        backup_file = filedialog.askopenfilename(
            title="选择要导入的灵魂备份 (.tar.gz)",
            initialdir=DOWNLOADS_DIR,
            filetypes=[("Compressed Backup", "*.tar.gz")]
        )
        if not backup_file:
            return

        if messagebox.askyesno("记忆重载", "导入操作将深度覆盖现有的所有上下文和系统记忆。\n准备好重载灵魂了吗？"):
            self.update_status("正在重置基底并注入记忆，请勿关闭窗口...")
            self.backup_btn.config(state=tk.DISABLED)
            self.restore_btn.config(state=tk.DISABLED)
            threading.Thread(target=self.run_restore, args=(backup_file,)).start()

    def run_restore(self, file_path):
        try:
            if not os.path.exists(SOURCE_DIR):
                os.makedirs(SOURCE_DIR)

            with tarfile.open(file_path, "r:gz") as tar:
                tar.extractall(path=SOURCE_DIR)
            
            self.update_status("✓ 灵魂已注入完成", color="#4CAF50")
            messagebox.showinfo("成功", "新记忆已注入成功！你的智能体已满血复活。")
        except Exception as e:
            self.update_status("✗ 恢复失败", color="#F44336")
            messagebox.showerror("错误", f"恢复过程中出错: {str(e)}")
        finally:
            self.backup_btn.config(state=tk.NORMAL)
            self.restore_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = AntigravitySoulManager(root)
    root.mainloop()

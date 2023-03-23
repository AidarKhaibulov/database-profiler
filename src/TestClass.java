import org.junit.Test;
import org.junit.jupiter.api.DisplayName;

import static org.junit.Assert.assertEquals;

public class TestClass {
    @Test
    @DisplayName("Simple cipher with full last block")
    public void simpleTest1() {
        CipherManager cm = new CipherManager(1);
        assertEquals("cadbgehf", cm.applyCipherToString("abcdefgh"));
    }
    @Test
    @DisplayName("Simple cipher with adding zeros")
    public void simpleTest2() {
        CipherManager cm = new CipherManager(1);
        assertEquals("cadbgehf\0p\0q", cm.applyCipherToString("abcdefghpq"));
    }
    @Test
    @DisplayName("Simple cipher without adding zeros")
    public void simpleTest3() {
        CipherManager cm = new CipherManager(2);
        assertEquals("cadbgehfpq", cm.applyCipherToString("abcdefghpq"));
    }
    @Test
    @DisplayName("Simple cipher many elements without adding zeros")
    public void simpleTest4() {
        CipherManager cm = new CipherManager(3);
        assertEquals("ccaaddbbppqq", cm.applyCipherToString("aabbccddppqq"));
    }
    @Test
    @DisplayName("Simple cipher many elements with adding zeros")
    public void simpleTest5() {
        CipherManager cm = new CipherManager(4);
        assertEquals("ccaaddbb\0\0pp\0\0qq", cm.applyCipherToString("aabbccddppqq"));
    }

}
